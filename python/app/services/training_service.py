import os
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.models.training import TrainingPlan
from app.models.exercise import Exercise
from app.schemas.training import TrainingPlanCreate
import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from tempfile import NamedTemporaryFile
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FBW_MUSCLES = ["Chest", "Back", "Legs", "Shoulders", "Arms"]

REP_RANGES = {
    "Siła": {"COMPOUND": "4-6", "ISOLATION": "6-8"},
    "Masa": {"COMPOUND": "6-10", "ISOLATION": "10-15"},
    "Redukcja": {"COMPOUND": "12-15", "ISOLATION": "15-20"},
}

SETS_BY_DIFFICULTY = {
    "beginner": 3,
    "intermediate": 4,
    "advanced": 5,
}

def get_exercise_type(exercise: Exercise) -> str:
    raw_type = getattr(exercise, "exercise_type", "COMPOUND")
    return raw_type.upper() if isinstance(raw_type, str) else "COMPOUND"

def generate_training_pdf(name: str, text_description: str) -> str:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(BASE_DIR, "..", "assets", "fonts", "DejaVuSans.ttf")
    font_path = os.path.abspath(font_path)
    pdfmetrics.registerFont(TTFont("DejaVu", font_path))

    temp = NamedTemporaryFile(delete=False, suffix=".pdf", prefix="training_", dir=".")
    c = canvas.Canvas(temp.name, pagesize=A4)
    width, height = A4

    c.setFont("DejaVu", 11)
    c.setTitle(name)
    margin = 40
    y = height - margin

    lines = text_description.split("\n")

    for line in lines:
        wrapped = split_text(line, 100)
        for subline in wrapped:
            c.drawString(margin, y, subline)
            y -= 15
            if y < margin:
                c.showPage()
                c.setFont("DejaVu", 11)
                y = height - margin

    c.save()
    return temp.name

def split_text(text, max_len):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= max_len:
            line += " " + word if line else word
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines

def generate_training_plan_demo_fbw(db: Session, user_id: int, plan_data: TrainingPlanCreate):
    if plan_data.split_type != "FBW":
        return JSONResponse(status_code=400, content={"error": "Wersja demo obsługuje tylko split FBW."})

    goal_key = plan_data.goal.capitalize()
    difficulty_key = plan_data.difficulty.lower()
    used_exercise_ids = set()
    training_plan_structure = []
    arm_days_used = 0

    for day in range(plan_data.days_per_week):
        day_plan = {"day": day + 1, "exercises": []}
        exercises_in_day = 0
        max_exercises = 6
        min_exercises = 4

        for muscle in FBW_MUSCLES:
            if exercises_in_day >= max_exercises:
                break

            if muscle == "Arms":
                if plan_data.goal == "Siła" and arm_days_used >= 2:
                    continue
                elif plan_data.goal in {"Masa", "Redukcja"} and day % 2 != 0:
                    continue

            muscle_name = muscle
            exercises = []

            if muscle == "Arms":
                biceps = db.query(Exercise).filter(
                    Exercise.muscle_group == "Biceps",
                    Exercise.difficulty == plan_data.difficulty
                ).all()
                triceps = db.query(Exercise).filter(
                    Exercise.muscle_group == "Triceps",
                    Exercise.difficulty == plan_data.difficulty
                ).all()
                exercises = biceps + triceps
            else:
                exercises = db.query(Exercise).filter(
                    Exercise.muscle_group == muscle,
                    Exercise.difficulty == plan_data.difficulty
                ).all()

            exercises = [ex for ex in exercises if ex.id not in used_exercise_ids]
            if not exercises:
                continue

            random.shuffle(exercises)
            ex = exercises[0]
            used_exercise_ids.add(ex.id)

            ex_type = get_exercise_type(ex)
            reps = REP_RANGES[goal_key].get(ex_type, "10-12")
            sets = SETS_BY_DIFFICULTY.get(difficulty_key, 4)

            day_plan["exercises"].append({
                "muscle": muscle_name,
                "name": ex.name,
                "sets": sets,
                "reps": reps
            })
            exercises_in_day += 1

            if muscle == "Arms":
                arm_days_used += 1

        if exercises_in_day < min_exercises:
            continue

        training_plan_structure.append(day_plan)

    text_description = f" Plan: {plan_data.name}\n Cel: {plan_data.goal}\n Split: FBW\n Dni: {plan_data.days_per_week}\n Poziom: {plan_data.difficulty.capitalize()}\n\n"
    for day in training_plan_structure:
        text_description += f" Dzień {day['day']}:\n"
        for ex in day["exercises"]:
            text_description += f" {ex['muscle']}: {ex['name']} | {ex['sets']}x{ex['reps']}\n"
        text_description += "\n"

    plan = TrainingPlan(
        user_id=user_id,
        name=plan_data.name,
        split_type="FBW",
        goal=plan_data.goal,
        days_per_week=plan_data.days_per_week,
        difficulty=plan_data.difficulty,
        text_description=text_description
    )
    db.add(plan)
    db.commit()
    db.refresh(plan)

    pdf_path = generate_training_pdf(plan_data.name, text_description)

    return {
        "training_plan": training_plan_structure,
        "summary": {
            "name": plan_data.name,
            "goal": plan_data.goal,
            "split": "FBW",
            "days": plan_data.days_per_week,
            "difficulty": plan_data.difficulty
        },
        "text_description": text_description,
        "pdf_path": pdf_path
    }
