from flask_wtf import FlaskForm
from wtforms.fields import SelectField, StringField, SubmitField 
from wtforms.validators import  ValidationError, DataRequired

class CourseForm(FlaskForm):
    major = SelectField(label= "Please select major:", choices = ['CptS', 'EE','MATH','ME', 'CHE'],validators=[DataRequired()])
    coursenum = StringField(label= "Please enter course number:", validators=[DataRequired()])
    title = StringField(label= "Please enter course title:", validators=[DataRequired()])
    submit = SubmitField('Submit')