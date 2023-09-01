
from app import db,app
from app.models import Course, Room, TeachingAssistant, TA_Assignment
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

#create a new TA_Assignment
newTAship = TA_Assignment(course_id = thecourse.id, ta_id = newTA.id)  #not providing the assign date, will use default value

# add newTAship as a new assignment for thecourse
thecourse.ta_positions.append(newTAship)

#check the courses of the newTAship
newTAship.course_assigned

#check the TAships of the TA
newTA.taships

# thecourse.ta_positions[0].ta_assigned

# newTA.taships[0].course_assigned
