from app import db
from datetime import datetime

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    coursenum = db.Column(db.String(3))  
    title = db.Column(db.String(150))
    major = db.Column(db.String(20))
    roomid = db.Column(db.Integer,db.ForeignKey('room.id'))
    ta_positions = db.relationship('TA_Assignment',back_populates="course_assigned")

    def __repr__(self):
        return '<Course {},{},{},{} >'.format(self.id, self.coursenum, self.title, self.major)
    
    def add_ta(self,newta):
        if not self.is_ta(newta):
            new_assignment = TA_Assignment( ta_assigned = newta)
            self.ta_positions.append(new_assignment)
            db.session.commit()

    def is_ta(self,newta):
        return  (TA_Assignment.query.filter_by(course_id=self.id).filter_by(ta_id=newta.id).count() > 0)

    def all_tas(self):
        return self.ta_positions

    def get_assignment_date(self, the_ta):
        if self.is_ta(the_ta):
            return TA_Assignment.query.filter_by(course_id=self.id).filter_by(ta_id=the_ta.id).first().assign_date
        else:
            return None 

    

class TeachingAssistant(db.Model):
    __tablename__ = 'teachingassistant'
    id = db.Column(db.Integer, primary_key = True)
    ta_name =  db.Column(db.String(100))
    taships = db.relationship('TA_Assignment', back_populates = 'ta_assigned')
    def __repr__(self):
        return '<TA {} - {} {} - {};>'.format(self.id,self.firstname, self.lastname)

class TA_Assignment(db.Model):
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    ta_id = db.Column(db.Integer, db.ForeignKey('teachingassistant.id'), primary_key=True)
    assign_date = db.Column(db.DateTime, default=datetime.utcnow)
    course_assigned = db.relationship('Course')
    ta_assigned = db.relationship('TeachingAssistant')
    def __repr__(self):
        return '<TA_Assignment ta: {} course: {} date: {}>'.format(self.ta_assigned,self.course_assigned, self.assign_date)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.String(50)) 
    roomNumber = db.Column(db.String(20))   
    capacity = db.Column(db.Integer)
    courses = db.relationship('Course', backref = 'classroom', lazy = "dynamic")
