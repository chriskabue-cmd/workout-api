from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from models import db, Workout, Exercise, WorkoutExercise
from schemas import WorkoutSchema, ExerciseSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)


# ------------------ WORKOUT ROUTES ------------------

@app.get("/workouts")
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts))


@app.get("/workouts/<int:id>")
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return workout_schema.dump(workout)


@app.post("/workouts")
def create_workout():
    try:
        data = request.get_json()
        workout = Workout(**data)
        db.session.add(workout)
        db.session.commit()
        return workout_schema.dump(workout), 201
    except Exception as e:
        return {"error": str(e)}, 400


@app.delete("/workouts/<int:id>")
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return {}, 204


# ------------------ EXERCISE ROUTES ------------------

@app.get("/exercises")
def get_exercises():
    return exercises_schema.dump(Exercise.query.all())


@app.get("/exercises/<int:id>")
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    return exercise_schema.dump(exercise)


@app.post("/exercises")
def create_exercise():
    try:
        data = request.get_json()
        exercise = Exercise(**data)
        db.session.add(exercise)
        db.session.commit()
        return exercise_schema.dump(exercise), 201
    except Exception as e:
        return {"error": str(e)}, 400


@app.delete("/exercises/<int:id>")
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    db.session.delete(exercise)
    db.session.commit()
    return {}, 204


# ------------------ ADD EXERCISE TO WORKOUT ------------------

@app.post("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
def add_exercise(workout_id, exercise_id):
    data = request.get_json()

    we = WorkoutExercise(
        workout_id=workout_id,
        exercise_id=exercise_id,
        reps=data.get("reps"),
        sets=data.get("sets"),
        duration_seconds=data.get("duration_seconds")
    )

    db.session.add(we)
    db.session.commit()

    return {"message": "Exercise added to workout"}, 201


if __name__ == "__main__":
    app.run(debug=True, port=5555)

with app.app_context():
    db.create_all()    