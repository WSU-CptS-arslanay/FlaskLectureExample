from app import db

assigned = db.Table('assigned',
    db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
    db.Column('ta_id', db.Integer, db.ForeignKey('teachingassistant.id'))
)

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    coursenum = db.Column(db.String(3))  
    title = db.Column(db.String(150))
    major = db.Column(db.String(20))
    roomid = db.Column(db.Integer,db.ForeignKey('room.id'))
    tas = db.relationship(
        'TeachingAssistant', secondary=assigned,
        primaryjoin=(assigned.c.course_id == id), lazy='dynamic', overlaps="courses")
    def __repr__(self):
        return '<Course {},{},{},{} >'.format(self.id, self.coursenum, self.title, self.major)
    
    def add_ta(self,newta):
        if not self.is_ta(newta):
            self.tas.append(newta)

    def is_ta(self,newta):
        return self.tas.filter(assigned.c.ta_id == newta.id).count() > 0

    def all_tas(self):
        return self.tas

class TeachingAssistant(db.Model):
    __tablename__ = 'teachingassistant'
    id = db.Column(db.Integer, primary_key = True)
    ta_name =  db.Column(db.String(100))
    courses = db.relationship(
        'Course', secondary=assigned,
        primaryjoin=(assigned.c.ta_id == id), lazy='dynamic', overlaps="tas")

    def __repr__(self):
        return '<TA {} - {} {} - {};>'.format(self.id,self.firstname, self.lastname)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.String(50)) 
    roomNumber = db.Column(db.String(20))   
    capacity = db.Column(db.Integer)
    courses = db.relationship('Course', backref = 'classroom', lazy = "dynamic")
