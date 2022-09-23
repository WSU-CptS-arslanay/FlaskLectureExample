from flask_wtf import FlaskForm
from wtforms.fields import SelectField, StringField, SubmitField 
from wtforms.validators import  ValidationError, DataRequired
from wtforms_sqlalchemy.fields import  QuerySelectField
from app.models import Course, Room

def get_rooms():
    return Room.query.all()

def getRoomLabel(theroom):
    return "{} - {}".format(theroom.building, theroom.roomNumber)

class CourseForm(FlaskForm):
    major = SelectField(label= "Please select major:", choices = ['CptS', 'EE','MATH','ME', 'CHE'],validators=[DataRequired()])
    coursenum = StringField(label= "Please enter course number:", validators=[DataRequired()])
    title = StringField(label= "Please enter course title:", validators=[DataRequired()])
    classroom = QuerySelectField('Classroom', query_factory = get_rooms, get_label = getRoomLabel , allow_blank=False)
    type = SelectField(label= "Please select course type:", choices = [(1,'In-person'), (2,'Online'), (3,'Video Conferencing'), (4,'Hybrid')])
    submit = SubmitField('Submit')


class TAForm(FlaskForm):
    ta_name = StringField(label= "TA name:", validators=[DataRequired()])
    submit = SubmitField('Submit')