from app import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coursenum = db.Column(db.String(3))  
    title = db.Column(db.String(150))
    major = db.Column(db.String(20))
    roomid = db.Column(db.Integer,db.ForeignKey('room.id'))
    classroom = db.relationship('Room', back_populates='courses')

    def __repr__(self):
        return '<Course {},{},{},{} >'.format(self.id, self.coursenum, self.title, self.major)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.String(50))
    roomNumber = db.Column(db.String(50))   
    capacity = db.Column(db.Integer)
    courses = db.relationship('Course', back_populates='classroom')
    def __repr__(self):
        return '<Room  id: {} - building: {}, room number: {}>'.format(self.id,self.building, self.roomNumber)
