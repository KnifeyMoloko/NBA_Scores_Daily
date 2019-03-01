from flask_wtf import FlaskForm
from wtforms import StringField


class DateForm(FlaskForm):
    date = StringField(label="score_date")
