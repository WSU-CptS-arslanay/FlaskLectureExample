from __future__ import print_function
import sys
from flask import render_template, flash, redirect, url_for, request

from app import app,db
from app.forms import CourseForm
from app.models import Course, Room

@app.before_request
def initDB(*args, **kwargs):
    if app._got_first_request:
        db.create_all()
        # create the rooms 
        allrooms = [{'building' : 'Fuller', 'roomNumber' : 'B46', 'capacity' : 60}, 
                    {'building' : 'UnityHall', 'roomNumber' : '175', 'capacity' : 100},
                    {'building' : 'UnityHall', 'roomNumber' : '150', 'capacity' : 80}]
        if Room.query.count() == 0:
            for room in allrooms:
                theroom = Room (building = room['building'],roomNumber=room['roomNumber'], capacity = room['capacity'] ) 
                db.session.add(theroom)
                db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def index():  
    form = CourseForm()
    if form.validate_on_submit():
        if (form.major.data is not None) and (form.coursenum.data is not None):
            #check if course already exists
            _coursecount = Course.query.filter_by(major=form.major.data).filter_by(coursenum=form.coursenum.data).count()
            #print(form.classroom.data)
            if _coursecount < 1:
                newcourse = Course(major = form.major.data,coursenum = form.coursenum.data,title = form.title.data, roomid = form.classroom.data.id)
                db.session.add(newcourse)
                db.session.commit()
                return redirect(url_for('course',name="{}{}-{}".format(form.major.data,form.coursenum.data, form.title.data)))
    # display existing courses
    _courses = Course.query.order_by(Course.coursenum).order_by(Course.major). all()
    return render_template('index.html', form=form, courses = _courses)

@app.route('/course/<name>')
def course(name):
    return render_template('course.html', name=name)