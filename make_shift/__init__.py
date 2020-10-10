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

  indivshifts = set_list(workers)

  _ , spshifts = special(workers,specialjobs)
  # print(spshifts)

  # workers2, restshifts = rest(workers,spshifts)
  # # print(workers2)
  # # print(restshifts)

  # shifts = restshifts + spshifts
  # indivshifts = classify(shifts,indivshifts)


  # workers3, _ = special(workers2,specialjobs)
  # # print(workers3)

  # normalshifts = normal(workers3,Jobs,indivshifts)
  # # print(normalshifts)

  # shift = normalshifts
  # # shifts = normalshifts + restshifts + spshifts

  # # print(shifts)

  # # indivshifts = Classify(shifts,Worker)
  # # indivshifts = Classify(shifts,indivshifts)
  # viewindivs = []
  # for indivs in indivshifts:
  #   tmp = []
  #   for inds in indivs:
  #     tmp.append(ind[0])
  #   viewindivs.append(tmp)
    

  # print(viewindivs)


if __name__ == '__main__':
  main()