from app import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coursenum = db.Column(db.String(3))  
    title = db.Column(db.String(150))
    major = db.Column(db.String(20))
    roomid = db.Column(db.Integer,db.ForeignKey('room.id'))
    #classroom : this relationship is autocreated by the backref in Room.courses relationship

    def __repr__(self):
        return '<Course {},{},{},{} >'.format(self.id, self.coursenum, self.title, self.major)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.String(50)) 
    roomNumber = db.Column(db.String(20))   
    capacity = db.Column(db.Integer)
    courses = db.relationship('Course', backref = 'classroom', lazy = "dynamic")
    def __repr__(self):
        return '<Room {},{},{},{} >'.format(self.id, self.building, self.roomNumber, self.capacity)