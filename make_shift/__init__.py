from make_shift.normal import normal
from make_shift.special import special
from make_shift.rest import rest

def main(workers,jobs,spjobs,config):
  # for worker in workers:
  #   worker.shift_init()

  spshifts = special(workers,spjobs,config)

  # print(spshifts)

  restshifts = rest(workers,config)

  # for worker in workers:
  #   print(worker.workername,worker.indivshifts)
  # print(restshifts)


  normalshifts = normal(workers,jobs,config)
  # print(normalshifts)

  for worker in workers:
    worker.indivshifts = sorted(worker.indivshifts,key=lambda x:(x.starttime))
  
  shifts = spshifts + restshifts + normalshifts

  return workers , shifts
  

  # for worker in workers:
  #   print(worker.workername,worker.indivshifts)
    


if __name__ == '__main__':
  main()