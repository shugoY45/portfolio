from flask_schedule import db
from flask_schedule.models import Worker, Job

workers = Worker.query.all()
jobs = Job.query.all()

# print(jobs)
# for worker in workers:
#   print(worker.workername)

def test():
  for job in jobs:
    print(job.priorty)