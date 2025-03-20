from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine
from app.models.exercise import Exercise, MuscleSize, MovementType, DifficultyLevel, ExerciseType
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

print(f"Using database: {engine.url}")

def seed_exercises(db: Session):
    """Dodaje 60 ćwiczeń do bazy danych z opisami"""
    exercises = [
        # ✅ KLATKA PIERSIOWA (Chest) - 10 ćwiczeń
        Exercise(name="Wyciskanie sztangi na ławce", muscle_group="Chest", muscle_size=MuscleSize.LARGE,
                 movement_type=MovementType.PUSH, difficulty=DifficultyLevel.INTERMEDIATE, 
                 exercise_type=ExerciseType.COMPOUND, recommended_reps={"masa": "6-12", "siła": "3-6", "redukcja": "12-15"},
                 recommended_sets={"beginner": "3", "intermediate": "4", "advanced": "5"}, rest_time=90,
                 description="Podstawowe ćwiczenie na klatkę piersiową, angażujące triceps i przednią część barków."),
        Exercise(name="Pompki klasyczne", muscle_group="Chest", muscle_size=MuscleSize.LARGE,
                 movement_type=MovementType.PUSH, difficulty=DifficultyLevel.BEGINNER,
                 exercise_type=ExerciseType.COMPOUND, recommended_reps={"masa": "10-15", "siła": "8-12", "redukcja": "15-20"},
                 recommended_sets={"beginner": "3", "intermediate": "4", "advanced": "5"}, rest_time=30,
                 description="Ćwiczenie na klatkę piersiową i triceps wykonywane z własnym ciężarem ciała."),
        Exercise(name="Dipy na poręczach", muscle_group="Chest", muscle_size=MuscleSize.LARGE,
                 movement_type=MovementType.PUSH, difficulty=DifficultyLevel.INTERMEDIATE,
                 exercise_type=ExerciseType.COMPOUND, recommended_reps={"masa": "6-12", "siła": "4-6", "redukcja": "12-15"},
                 recommended_sets={"beginner": "3", "intermediate": "4", "advanced": "5"}, rest_time=90,
                 description="Ćwiczenie na klatkę piersiową i triceps, szczególnie efektywne przy pogłębieniu ruchu."),
        Exercise(name="Wyciskanie hantli na skosie dodatnim", muscle_group="Chest", muscle_size=MuscleSize.LARGE,
                 movement_type=MovementType.PUSH, difficulty=DifficultyLevel.INTERMEDIATE, 
                 exercise_type=ExerciseType.COMPOUND, recommended_reps={"masa": "8-12", "siła": "6-10", "redukcja": "12-15"},
                 recommended_sets={"beginner": "3", "intermediate": "4", "advanced": "5"}, rest_time=90,
                 description="Ćwiczenie na górną część klatki piersiowej, wykonywane hantlami."),
        Exercise(name="Rozpiętki na ławce płaskiej", muscle_group="Chest", muscle_size=MuscleSize.LARGE,
                 movement_type=MovementType.PUSH, difficulty=DifficultyLevel.BEGINNER, 
                 exercise_type=ExerciseType.ISOLATION, recommended_reps={"masa": "10-15", "siła": "8-12", "redukcja": "12-15"},
                 recommended_sets={"beginner": "3", "intermediate": "4", "advanced": "5"}, rest_time=60,
                 description="Ćwiczenie izolacyjne na klatkę piersiową, poprawiające jej kształt."),
        
        # ✅ PLECY (Back) - 10 ćwiczeń
        Exercise(name="Podciąganie nachwytem", muscle_group="Back", muscle_size=MuscleSize.LARGE,
                 movement_type=MovementType.PULL, difficulty=DifficultyLevel.INTERMEDIATE, 
                 exercise_type=ExerciseType.COMPOUND, recommended_reps={"masa": "6-12", "siła": "3-6", "redukcja": "12-15"}, 
                 recommended_sets={"beginner": "3", "intermediate": "4", "advanced": "5"}, rest_time=120,
                 description="Ćwiczenie na rozwój szerokości pleców, angażujące bicepsy i przedramiona."),
        Exercise(name="Wiosłowanie sztangą", muscle_group="Back", muscle_size=MuscleSize.LARGE,
                 movement_type=MovementType.PULL, difficulty=DifficultyLevel.INTERMEDIATE, 
                 exercise_type=ExerciseType.COMPOUND, recommended_reps={"masa": "6-12", "siła": "4-6", "redukcja": "12-15"}, 
                 recommended_sets={"beginner": "3", "intermediate": "4", "advanced": "5"}, rest_time=90,
                 description="Jedno z najlepszych ćwiczeń na grubość pleców, angażujące dolną i środkową część mięśni grzbietu."),
        
        # ✅ NOGI (Legs) - 10 ćwiczeń
        Exercise(name="Przysiad ze sztangą", muscle_group="Legs", muscle_size=MuscleSize.LARGE,
                 movement_type=MovementType.PUSH, difficulty=DifficultyLevel.INTERMEDIATE, 
                 exercise_type=ExerciseType.COMPOUND, recommended_reps={"masa": "6-12", "siła": "3-6", "redukcja": "12-15"}, 
                 recommended_sets={"beginner": "3", "intermediate": "4", "advanced": "5"}, rest_time=120,
                 description="Najlepsze ćwiczenie na rozwój mięśni nóg, angażujące również core i dolny grzbiet."),
        
        # ✅ BICEPS - 10 ćwiczeń
        Exercise(name="Uginanie ramion ze sztangą", muscle_group="Biceps", muscle_size=MuscleSize.SMALL,
                 movement_type=MovementType.PULL, difficulty=DifficultyLevel.BEGINNER,
                 exercise_type=ExerciseType.ISOLATION, recommended_reps={"masa": "8-12", "siła": "6-10", "redukcja": "12-15"},
                 recommended_sets={"beginner": "3", "intermediate": "4", "advanced": "5"}, rest_time=60,
                 description="Podstawowe ćwiczenie na masę bicepsów, angażujące oba ramiona jednocześnie."),
        
        # ✅ TRICEPS - 10 ćwiczeń
        Exercise(name="Wyciskanie francuskie sztangi", muscle_group="Triceps", muscle_size=MuscleSize.SMALL,
                 movement_type=MovementType.PUSH, difficulty=DifficultyLevel.INTERMEDIATE, 
                 exercise_type=ExerciseType.ISOLATION, recommended_reps={"masa": "8-12", "siła": "6-10", "redukcja": "12-15"},
                 recommended_sets={"beginner": "3", "intermediate": "4", "advanced": "5"}, rest_time=60,
                 description="Ćwiczenie izolacyjne na triceps, wykonywane ze sztangą w leżeniu."),
        
        # ✅ BARKI (Shoulders) - 10 ćwiczeń
        Exercise(name="Wyciskanie żołnierskie", muscle_group="Shoulders", muscle_size=MuscleSize.LARGE,
                 movement_type=MovementType.PUSH, difficulty=DifficultyLevel.INTERMEDIATE, 
                 exercise_type=ExerciseType.COMPOUND, recommended_reps={"masa": "6-12", "siła": "4-6", "redukcja": "12-15"},
                 recommended_sets={"beginner": "3", "intermediate": "4", "advanced": "5"}, rest_time=90,
                 description="Ćwiczenie na mięśnie naramienne, wykonywane sztangą nad głowę."),
    ]

    for exercise in exercises:
        db.add(exercise)

    db.commit()
    print(f"✅ Dodano {len(exercises)} ćwiczeń do bazy!")

if __name__ == "__main__":
    db = SessionLocal()
    seed_exercises(db)
    db.close()
