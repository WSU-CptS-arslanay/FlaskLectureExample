from app import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coursenum = db.Column(db.String(3))  
    title = db.Column(db.String(150))
    major = db.Column(db.String(20))
    def __repr__(self):
        return '<Course {},{},{},{} >'.format(self.id, self.coursenum, self.title, self.major)