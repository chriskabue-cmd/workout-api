# workout-api

## Description
Backend API for managing workouts and exercises.

## Project structure
server/
│
├── app.py
├── models.py
├── schemas.py
├── seed.py

## Installation Instructions
1. Clone the repository
git clone https://github.com/chriskabue-cmd/workout-api.git
cd workout-api

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