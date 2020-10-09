from flask_schedule import db
from flask_schedule.models import Worker

workers = Worker.query.all()
print(workers)