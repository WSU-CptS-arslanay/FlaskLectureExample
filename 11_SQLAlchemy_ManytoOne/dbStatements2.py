
from app import db,app
from app.models import Course, Room
app.app_context().push()
db.create_all()

# create Room and write it to DB
newroom = Room(building='Sloan',roomNumber='175', capacity=100)
db.session.add(newroom)
db.session.commit()

# create Course and write it to DB
newCourse = Course(major='CptS',coursenum='322', title='Software Engineering', roomid = newroom.id)
db.session.add(newCourse)
db.session.commit()

# get the Course object for CptS 322
thecourse = Course.query.filter_by(major='CptS').filter_by(coursenum='322').first()

