from setting import *
from make_shift.function import set_list, classify
from make_shift.normal import normal
from make_shift.special import special
from make_shift.rest import rest
from flask_schedule.models import Worker, Job, SpecialJob

def main():
  workers = Worker.query.all()
  jobs = Job.query.all()
  specialjobs = SpecialJob.query.all()
  for worker in workers:
    worker.init()

  spshifts = special(workers,specialjobs)

  # print(spshifts)

  restshifts = rest(workers)

  # for worker in workers:
  #   print(worker.workername,worker.indivshifts)
  # print(restshifts)


  normalshifts = normal(workers,jobs)
  # print(normalshifts)

  for worker in workers:
    print(worker.workername,worker.indivshifts)
    


if __name__ == '__main__':
  main()