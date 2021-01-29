from make_shift.normal import normal
from make_shift.special import special
from make_shift.rest import rest
from make_shift.function import evaluation
import random

def main(workers,jobs,spjobs,config):
  #シフトの初期値の作成
  # spshifts = special(workers,spjobs,config)
  # restshifts = rest(workers,config)
  # normalshifts = normal(workers,jobs,config)
  # shifts = spshifts + restshifts + normalshifts

  #目的関数を最小化する
  # shifts = minimize(workers,jobs,spjobs,config)

  #山登り法を用いた最小化
  #スケジュールの点数を格納する
  opentime = config.store_opentime
  closetime = config.store_closetime
  hour_list = [i for i in range(opentime.hour,closetime.hour)]
  one_date = workers[0].one_date.date()

  minscore = 0
  normalshifts = []

  for i in range(10):
    for worker in workers:
      worker.starttime = worker.starttime.time()
      worker.endtime = worker.endtime.time()
      worker.shift_init(one_date)
    random.shuffle(hour_list)
    spshifts = special(workers,spjobs,config)
    restshifts = rest(workers,config)
    prenormalshifts = normal(workers,jobs,config,hour_list)
    preshifts = spshifts + restshifts + prenormalshifts
    score = evaluation(preshifts,workers)
    # print(score)
    if minscore == 0:
      minscore = score
      shifts = preshifts
    elif minscore > score:
      minscore = score
      shifts = preshifts
  # print(minscore)
  # print(shifts)

  return shifts
  
    


if __name__ == '__main__':
  main()