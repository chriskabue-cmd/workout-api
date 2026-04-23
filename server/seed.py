from app import app
from models import db, Workout, Exercise, WorkoutExercise
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    pushup = Exercise(name="Push Up", category="strength", equipment_needed=False)
    running = Exercise(name="Running", category="cardio", equipment_needed=False)

    workout = Workout(date=date.today(), duration_minutes=45, notes="Morning session")

    db.session.add_all([pushup, running, workout])
    db.session.commit()

    we = WorkoutExercise(
        workout_id=workout.id,
        exercise_id=pushup.id,
        reps=15,
        sets=3
    )

    db.session.add(we)
    db.session.commit()

    print("Seeded successfully!")