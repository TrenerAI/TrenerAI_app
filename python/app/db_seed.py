from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine
from app.models.exercise import Exercise, MuscleSize, DifficultyLevel, ExerciseType
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

print(f"Using database: {engine.url}")

def generate_exercises_for_group(name_prefix, muscle_group, muscle_size, difficulty, exercise_type):
    exercises = []
    for i in range(1, 11):
        exercises.append(
            Exercise(
                name=f"{name_prefix} {i} ({difficulty.value})",
                muscle_group=muscle_group,
                muscle_size=muscle_size,
                difficulty=difficulty,
                exercise_type=exercise_type
            )
        )
    return exercises

def seed_exercises(db: Session):
    all_exercises = []

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na klatkę",
        muscle_group="Chest",
        muscle_size=MuscleSize.LARGE,
        difficulty=DifficultyLevel.INTERMEDIATE,
        exercise_type=ExerciseType.COMPOUND
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na plecy",
        muscle_group="Back",
        muscle_size=MuscleSize.LARGE,
        difficulty=DifficultyLevel.INTERMEDIATE,
        exercise_type=ExerciseType.COMPOUND
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na nogi",
        muscle_group="Legs",
        muscle_size=MuscleSize.LARGE,
        difficulty=DifficultyLevel.INTERMEDIATE,
        exercise_type=ExerciseType.COMPOUND
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na barki",
        muscle_group="Shoulders",
        muscle_size=MuscleSize.LARGE,
        difficulty=DifficultyLevel.INTERMEDIATE,
        exercise_type=ExerciseType.COMPOUND
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na biceps",
        muscle_group="Biceps",
        muscle_size=MuscleSize.SMALL,
        difficulty=DifficultyLevel.INTERMEDIATE,
        exercise_type=ExerciseType.ISOLATION
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na triceps",
        muscle_group="Triceps",
        muscle_size=MuscleSize.SMALL,
        difficulty=DifficultyLevel.INTERMEDIATE,
        exercise_type=ExerciseType.ISOLATION
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na klatkę",
        muscle_group="Chest",
        muscle_size=MuscleSize.LARGE,
        difficulty=DifficultyLevel.BEGINNER,
        exercise_type=ExerciseType.COMPOUND
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na plecy",
        muscle_group="Back",
        muscle_size=MuscleSize.LARGE,
        difficulty=DifficultyLevel.BEGINNER,
        exercise_type=ExerciseType.COMPOUND
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na nogi",
        muscle_group="Legs",
        muscle_size=MuscleSize.LARGE,
        difficulty=DifficultyLevel.BEGINNER,
        exercise_type=ExerciseType.COMPOUND
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na barki",
        muscle_group="Shoulders",
        muscle_size=MuscleSize.LARGE,
        difficulty=DifficultyLevel.BEGINNER,
        exercise_type=ExerciseType.COMPOUND
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na biceps",
        muscle_group="Biceps",
        muscle_size=MuscleSize.SMALL,
        difficulty=DifficultyLevel.BEGINNER,
        exercise_type=ExerciseType.ISOLATION
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na triceps",
        muscle_group="Triceps",
        muscle_size=MuscleSize.SMALL,
        difficulty=DifficultyLevel.BEGINNER,
        exercise_type=ExerciseType.ISOLATION
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na klatkę",
        muscle_group="Chest",
        muscle_size=MuscleSize.LARGE,
        difficulty=DifficultyLevel.ADVANCED,
        exercise_type=ExerciseType.COMPOUND
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na plecy",
        muscle_group="Back",
        muscle_size=MuscleSize.LARGE,
        difficulty=DifficultyLevel.ADVANCED,
        exercise_type=ExerciseType.COMPOUND
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na nogi",
        muscle_group="Legs",
        muscle_size=MuscleSize.LARGE,
        difficulty=DifficultyLevel.ADVANCED,
        exercise_type=ExerciseType.COMPOUND
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na barki",
        muscle_group="Shoulders",
        muscle_size=MuscleSize.LARGE,
        difficulty=DifficultyLevel.ADVANCED,
        exercise_type=ExerciseType.COMPOUND
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na biceps",
        muscle_group="Biceps",
        muscle_size=MuscleSize.SMALL,
        difficulty=DifficultyLevel.ADVANCED,
        exercise_type=ExerciseType.ISOLATION
    )

    all_exercises += generate_exercises_for_group(
        name_prefix="Ćwiczenie na triceps",
        muscle_group="Triceps",
        muscle_size=MuscleSize.SMALL,
        difficulty=DifficultyLevel.ADVANCED,
        exercise_type=ExerciseType.ISOLATION
    )

    for exercise in all_exercises:
        db.add(exercise)

    db.commit()
    print(f"✅ Dodano {len(all_exercises)} ćwiczeń do bazy!")


if __name__ == "__main__":
    db = SessionLocal()
    seed_exercises(db)
    db.close()
