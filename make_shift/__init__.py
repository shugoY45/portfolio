from setting import *
from make_shift.function import set_list, classify
from make_shift.normal import normal
from make_shift.special import special
from make_shift.rest import rest
from flask_schedule.models import Worker, Job

def main():
  workers = Worker.query.all()
  jobs = Job.query.all()

  indivshift = set_list(workers)

  _ , spshift = special(workers,specialjobs)
  # print(SpShift)

  worker2, restshift = Rest(worker,spshift)
  # print(Worker2)
  # print(RestShift)

  Shift = RestShift + SpShift
  IndivShift = Classify(Shift,IndivShift)


  Worker3, _ = Special(Worker2,SpecialJob)
  # print(Worker3)

  NormalShift = Normal(Worker3,Job,IndivShift)
  # print(NormalShift)

  shift = NormalShift
  # Shift = NormalShift + RestShift + SpShift

  # print(Shift)

  # IndivShift = Classify(Shift,Worker)
  # IndivShift = Classify(Shift,IndivShift)
  viewindivs = []
  for indivs in indivshift:
    tmp = []
    for inds in indivs:
      tmp.append(ind[0])
    viewindiv.append(tmp)
    

  # print(viewindivs)


if __name__ == '__main__':
  main()