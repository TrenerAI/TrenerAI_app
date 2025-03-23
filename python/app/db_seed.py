from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine
from app.models.exercise import Exercise, MuscleSize, MovementType, DifficultyLevel, ExerciseType
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

print(f"Using database: {engine.url}")

def generate_exercises_for_group(name_prefix, muscle_group, muscle_size, movement_type, difficulty, exercise_type, description_base, rest_time):
    exercises = []
    for i in range(1, 11):
        exercises.append(
            Exercise(
                name=f"{name_prefix} {i}",
                muscle_group=muscle_group,
                muscle_size=muscle_size,
                movement_type=movement_type,
                difficulty=difficulty,
                exercise_type=exercise_type,
                recommended_reps={"masa": "8-12", "siła": "6-10", "redukcja": "12-15"},
                recommended_sets={"beginner": "3", "intermediate": "4", "advanced": "5"},
                rest_time=rest_time,
                description=f"{description_base} ({i})"
            )
        )
    return exercises

def seed_exercises(db: Session):
    all_exercises = []

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na klatkę",
        muscle_group="Chest",
        muscle_size=MuscleSize.LARGE,
        movement_type=MovementType.PUSH,
        difficulty=DifficultyLevel.INTERMEDIATE,
        exercise_type=ExerciseType.COMPOUND,
        description_base="Ćwiczenie rozwijające mięśnie klatki piersiowej",
        rest_time=90
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na plecy",
        muscle_group="Back",
        muscle_size=MuscleSize.LARGE,
        movement_type=MovementType.PULL,
        difficulty=DifficultyLevel.INTERMEDIATE,
        exercise_type=ExerciseType.COMPOUND,
        description_base="Ćwiczenie rozwijające mięśnie grzbietu",
        rest_time=90
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na nogi",
        muscle_group="Legs",
        muscle_size=MuscleSize.LARGE,
        movement_type=MovementType.PUSH,
        difficulty=DifficultyLevel.INTERMEDIATE,
        exercise_type=ExerciseType.COMPOUND,
        description_base="Ćwiczenie na mięśnie nóg",
        rest_time=120
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na barki",
        muscle_group="Shoulders",
        muscle_size=MuscleSize.LARGE,
        movement_type=MovementType.PUSH,
        difficulty=DifficultyLevel.INTERMEDIATE,
        exercise_type=ExerciseType.COMPOUND,
        description_base="Ćwiczenie na mięśnie naramienne",
        rest_time=90
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na biceps",
        muscle_group="Biceps",
        muscle_size=MuscleSize.SMALL,
        movement_type=MovementType.PULL,
        difficulty=DifficultyLevel.BEGINNER,
        exercise_type=ExerciseType.ISOLATION,
        description_base="Ćwiczenie izolujące biceps",
        rest_time=60
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na triceps",
        muscle_group="Triceps",
        muscle_size=MuscleSize.SMALL,
        movement_type=MovementType.PUSH,
        difficulty=DifficultyLevel.INTERMEDIATE,
        exercise_type=ExerciseType.ISOLATION,
        description_base="Ćwiczenie izolujące triceps",
        rest_time=60
    )

    for exercise in all_exercises:
        db.add(exercise)

    db.commit()
    print(f"✅ Dodano {len(all_exercises)} ćwiczeń do bazy!")

if __name__ == "__main__":
    db = SessionLocal()
    seed_exercises(db)
    db.close()
