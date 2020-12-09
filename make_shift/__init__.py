from make_shift.normal import normal
from make_shift.special import special
from make_shift.rest import rest
# from make_shift.function import minimize

def main(workers,jobs,spjobs,config):
  #シフトの初期値の作成
  spshifts = special(workers,spjobs,config)
  restshifts = rest(workers,config)
  normalshifts = normal(workers,jobs,config)
  shifts = spshifts + restshifts + normalshifts

  #目的関数を最小化する
  # shifts = minimize(shifts,workers)
  
  return shifts
  
    


if __name__ == '__main__':
  main()