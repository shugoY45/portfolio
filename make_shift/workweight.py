from setting import *

worker_name = 0
work_start_time = 1
work_end_time = 2
work_weight = 3

indiv_workername = 0


def WorkWeight(Worker,IndivShift,hour):
  
  for worker in Worker:
    for indiv in IndivShift:
      if worker[worker_name] == indiv[indiv_workername]:
        i = 1


  return Worker