from make_shift.normal import normal
from make_shift.special import special
from make_shift.rest import rest
from make_shift.function import evaluation
import random

def main(workers,jobs,spjobs,config):

  #乱択山登り法を用いた最小化

  # 山登り法とは「現在の解の近傍の内で最も成績の良い解」を近傍解として選び、「現在の解より近傍解の成績の方が良い場合」に近傍解と現在の解を入れ換える方法であり、極値を見つけるのには適している。
  # この山登り法を乱択アルゴリズムとして、ランダムに探索開始の初期値を複数選び、探索が終了し極値が見つかった後、見つけた極値の中から最小値･最大値を選ぶことにより目的関数の最小値・最大値として近似する。
  # 本プログラムでは時間と従業員のlistの順番をランダムにすることでスケジューリングに多様性を持たせ、evoluate関数を用いて点数をつけることで最も良い点数のスケジュールを返している。
  
  one_date = workers[0].one_date.date()
  minscore = 0
  normalshifts = []

  # 時間配列作成
  opentime = config.store_opentime
  closetime = config.store_closetime
  hour_list = [i for i in range(opentime.hour,closetime.hour)]

  # 乱択アルゴリズムの初期値の個数
  T = 100

  for i in range(T):
    for worker in workers:
      worker.starttime = worker.starttime.time()
      worker.endtime = worker.endtime.time()
      worker.shift_init(one_date)
    # 乱択のためのシャッフル
    random.shuffle(hour_list)
    random.shuffle(workers)

    # スケジュールの作成
    spshifts = special(workers,spjobs,config)
    restshifts = rest(workers,config)
    prenormalshifts = normal(workers,jobs,config,hour_list)
    preshifts = spshifts + restshifts + prenormalshifts

    #スケジュール（preshifts）の点数をevoluate関数で評価し、最高得点の場合shiftsに格納。
    score = evaluation(preshifts,workers)
    if minscore == 0:
      minscore = score
      shifts = preshifts
    elif minscore > score:
      minscore = score
      shifts = preshifts

  return shifts
  
    


if __name__ == '__main__':
  main()