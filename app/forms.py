from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import Required

class SubmissionForm(FlaskForm):
    name = TextField("Name")
    size = TextField("Size")
    submit = SubmitField("Submit")
