
from app import db
from app.models import Course, Room
app.app_context().push()
db.create_all()
# create Course and write it to DB
newCourse = Course(major='CptS',coursenum='322', title='Software Engineering', roomid = 1)
db.session.add(newCourse)
newCourse = Course(major='CptS',coursenum='451', title='Database Systems', roomid = 1)
db.session.add(newCourse)
db.session.commit()

Course.query.all()
Course.query.filter_by(major='CptS').all()
Course.query.filter_by(major='CptS').first()
Course.query.filter_by(major='CptS').order_by(Course.title).all()
Course.query.filter_by(major='CptS').count()

# create Room and write it to DB
newroom = Room(building='Sloan',roomNumber='175', capacity=100)
db.session.add(newroom)
db.session.commit()

# query the classes for a room
theroom = Room.query.filter_by(id=1).first()
theroom = Room.query.filter_by(building = 'Sloan').filter_by(roomNumber=175).first()
# ???

# query the room for a class
thecourse = Course.query.filter_by(major='CptS').filter_by(coursenum='322').first()
## ???

