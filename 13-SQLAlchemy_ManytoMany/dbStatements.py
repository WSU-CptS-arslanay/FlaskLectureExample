
from app import db,app
from app.models import Course, Room, TeachingAssistant
app.app_context().push()
db.create_all()

# create Room and write it to DB
newroom = Room(building='Sloan',roomNumber='175', capacity=100)
db.session.add(newroom)
db.session.commit()

# create Course and write it to DB
newCourse = Course(major='CptS',coursenum='411', title='Parallel Processing', roomid = newroom.id)
db.session.add(newCourse)
db.session.commit()


# create a TA and write it to DB
newTA = TeachingAssistant(ta_name = 'Guangbei')
db.session.add(newTA)
db.session.commit()

# get the Course object for CptS 411
thecourse = Course.query.filter_by(major='CptS').filter_by(coursenum='411').first()

# add newTA as a new TA for thecourse
thecourse.tas.append(newTA)

#check the courses of the newTA
newTA.courses


# anotherTA = TeachingAssistant(ta_name = 'Zayn')
# db.session.add(anotherTA)
# db.session.commit()

# newCourse = Course(major='CptS',coursenum='302', title='Ethics', roomid = newroom.id)
# db.session.add(newCourse)
# db.session.commit()
# newCourse.tas.add(anotherTA)

# newCourse = Course(major='CptS',coursenum='327', title='Security', roomid = newroom.id)
# db.session.add(newCourse)
# db.session.commit()
# anotherTA.courses.add(newCourse)
# anotherTA.courses.all()
