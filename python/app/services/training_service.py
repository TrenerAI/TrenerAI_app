from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.models.training import TrainingPlan
from app.models.exercise import Exercise
from app.schemas.training import TrainingPlanCreate
import random
import json
import math

# 🏋️‍♂️ Maksymalna liczba serii na tydzień dla każdej partii mięśniowej
MUSCLE_VOLUME_LIMITS = {
    "Legs": (12, 24),
    "Back": (12, 24),
    "Chest": (10, 22),
    "Shoulders": (10, 20),
    "Biceps": (8, 16),
    "Triceps": (8, 16),
    "Core": (6, 15),
}

# 🔢 Maksymalna liczba serii w tygodniu dla różnych splitów
SPLIT_VOLUME_LIMITS = {
    "FBW": (10, 15),  # na partię
    "PPL": (16, 22),  # na partię
    "Góra-Dół": (14, 20),  # na partię
}

# 🔀 Podział grup mięśniowych dla różnych splitów
SPLIT_MAPPING = {
    "FBW": ["Chest", "Back", "Legs", "Shoulders", "Arms"],
    "PPL": {
        "Push": ["Chest", "Shoulders", "Triceps"],
        "Pull": ["Back", "Biceps"],
        "Legs": ["Legs"]
    },
    "Góra-Dół": {
        "Upper": ["Chest", "Back", "Shoulders", "Arms"],
        "Lower": ["Legs"]
    }
}

def generate_training_plan(db: Session, user_id: int, plan_data: TrainingPlanCreate):
    """Generowanie planu treningowego z uwzględnieniem limitu serii tygodniowych."""

    training_text = f"📅 **Plan treningowy: {plan_data.name}**\n"
    training_text += f"🔹 Cel: {plan_data.goal}\n"
    training_text += f"🔹 Split: {plan_data.split_type}\n"
    training_text += f"🔹 Dni w tygodniu: {plan_data.days_per_week}\n"
    training_text += f"🔹 Poziom: {plan_data.difficulty.capitalize()}\n\n"

    # 🔢 Limit serii na partię mięśniową dla danego splitu
    min_weekly_volume, max_weekly_volume = SPLIT_VOLUME_LIMITS.get(plan_data.split_type, (10, 15))

    # 📊 Obliczamy liczbę serii na dzień
    weekly_muscle_volume = {muscle: 0 for muscle in MUSCLE_VOLUME_LIMITS.keys()}

    for day in range(plan_data.days_per_week):
        training_text += f"**🗓️ Dzień {day+1}**\n"

        # Wybór partii mięśniowych na dany dzień
        if plan_data.split_type == "FBW":
            target_muscles = SPLIT_MAPPING["FBW"]
        elif plan_data.split_type == "PPL":
            target_muscles = list(SPLIT_MAPPING["PPL"].values())[day % 3]
        elif plan_data.split_type == "Góra-Dół":
            target_muscles = list(SPLIT_MAPPING["Góra-Dół"].values())[day % 2]
        else:
            target_muscles = []

        day_exercises = []
        for muscle in target_muscles:
            muscle_name = muscle

            # 🛠️ **Obsługa Arms → Biceps + Triceps**
            if muscle == "Arms":
                biceps_exercises = db.query(Exercise).filter(
                    Exercise.muscle_group == "Biceps",
                    Exercise.difficulty == plan_data.difficulty
                ).all()
                triceps_exercises = db.query(Exercise).filter(
                    Exercise.muscle_group == "Triceps",
                    Exercise.difficulty == plan_data.difficulty
                ).all()

                # Połącz ćwiczenia na biceps i triceps
                exercises = biceps_exercises + triceps_exercises
                muscle_name = "Biceps/Triceps"
            else:
                exercises = db.query(Exercise).filter(
                    Exercise.muscle_group == muscle,
                    Exercise.difficulty == plan_data.difficulty
                ).all()

            # Jeśli mamy dostępne ćwiczenia, losujemy ich ilość zależnie od limitu serii
            if exercises:
                # 🛠️ **Ustalamy dostępną objętość tygodniową**
                if muscle == "Arms":
                    remaining_biceps_volume = max_weekly_volume - weekly_muscle_volume.get("Biceps", 0)
                    remaining_triceps_volume = max_weekly_volume - weekly_muscle_volume.get("Triceps", 0)
                    remaining_volume = min(remaining_biceps_volume, remaining_triceps_volume)
                else:
                    remaining_volume = max_weekly_volume - weekly_muscle_volume.get(muscle, 0)

                max_series_per_exercise = min(math.ceil(remaining_volume / plan_data.days_per_week), 5)
                
                selected_exercises = random.sample(exercises, min(len(exercises), 3))
                day_exercises.extend(selected_exercises)

                for exercise in selected_exercises:
                    reps_data = exercise.recommended_reps
                    sets_data = exercise.recommended_sets

                    if isinstance(reps_data, str):
                        reps_data = json.loads(reps_data)
                    if isinstance(sets_data, str):
                        sets_data = json.loads(sets_data)

                    recommended_reps = reps_data.get(plan_data.goal, "10-12")
                    recommended_sets = min(int(sets_data.get(plan_data.difficulty, "3")), max_series_per_exercise)

                    # 🔄 **Aktualizujemy objętość dla Biceps i Triceps osobno**
                    if muscle == "Arms":
                        weekly_muscle_volume["Biceps"] += recommended_sets
                        weekly_muscle_volume["Triceps"] += recommended_sets
                    else:
                        weekly_muscle_volume[muscle] += recommended_sets

                    training_text += f"💪 {muscle_name}: {exercise.name} | {recommended_sets}x{recommended_reps}\n"

        if not day_exercises:
            training_text += "🚨 Brak dostępnych ćwiczeń dla tego dnia!\n"

        training_text += "\n"

    # ✅ **ZAPISUJEMY PLAN TRENINGOWY W BAZIE**
    plan = TrainingPlan(
        user_id=user_id,
        name=plan_data.name,
        split_type=plan_data.split_type,
        goal=plan_data.goal,
        days_per_week=plan_data.days_per_week,
        difficulty=plan_data.difficulty,
        text_description=training_text  
    )
    db.add(plan)
    db.commit()
    db.refresh(plan)

    return JSONResponse({"training_plan": training_text})
