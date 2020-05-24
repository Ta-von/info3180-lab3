from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    Name = StringField('Name', validators = [DataRequired()])
    Email = StringField('Email', validators = [DataRequired(), Email()])
    Subject = StringField('Subject', validators = [DataRequired()])
    Message = TextAreaField('Message', validators = [DataRequired()])
