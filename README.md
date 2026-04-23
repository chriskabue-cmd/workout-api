# workout-api

## Description
Backend API for managing workouts and exercises.

## Setup
pipenv install
pipenv shell

export FLASK_APP=server/app.py

flask db init
flask db migrate -m "init"
flask db upgrade

python server/seed.py

## Run
flask run

## Endpoints
GET /workouts
GET /workouts/<id>
POST /workouts
DELETE /workouts/<id>

GET /exercises
GET /exercises/<id>
POST /exercises
DELETE /exercises/<id>

POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises