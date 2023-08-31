import os
basedir = os.path.abspath(os.path.dirname(__file__))

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] =  'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'course.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from forms import CourseForm

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coursenum = db.Column(db.String(3))  
    title = db.Column(db.String(150))
    major = db.Column(db.String(20))
    def __repr__(self):
        return '<Course {},{},{},{} >'.format(self.id, self.coursenum, self.title, self.major)

@app.route('/', methods=['GET', 'POST'])
def index():  
    form = CourseForm()
    if form.validate_on_submit():
        if (form.major.data is not None) and (form.coursenum.data is not None):
            #check if course already exists
            _coursecount = Course.query.filter_by(major=form.major.data).filter_by(coursenum=form.coursenum.data).count()
            if _coursecount < 1:
                newcourse = Course(major = form.major.data,coursenum = form.coursenum.data,title = form.title.data)
                db.session.add(newcourse)
                db.session.commit()
                return redirect(url_for('course',name="{}{}-{}".format(form.major.data,form.coursenum.data, form.title.data)))
    # display existing courses
    _courses = Course.query.order_by(Course.coursenum).order_by(Course.major). all()
    return render_template('index.html', form=form, courses = _courses)

@app.route('/course/<name>')
def course(name):
    return render_template('course.html', name=name)
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)

