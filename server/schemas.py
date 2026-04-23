from marshmallow import Schema, fields, validates, ValidationError


# -------- Exercise --------
class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool()

    @validates('category')
    def validate_category(self, value):
        allowed = ["strength", "cardio", "flexibility"]
        if value.lower() not in allowed:
            raise ValidationError("Invalid category")


# -------- WorkoutExercise --------
class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()

    exercise = fields.Nested(ExerciseSchema)


# -------- Workout --------
class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()

    workout_exercises = fields.Nested(WorkoutExerciseSchema, many=True)