from setting import *
from datetime import datetime, timedelta
from flask_schedule.models import Shift


# 休憩シフト作成
def rest(workers):

  # 休憩が必要な人を探し、かつ始業時間と終業時間の平均時間を追加
  store_median = (datetime.strptime(store_opentime, '%H:%M').hour+datetime.strptime(store_closetime, '%H:%M').hour)/2
  for worker in workers:
    if datetime.strptime(worker.endtime, '%H:%M')-datetime.strptime(worker.starttime, '%H:%M') > timedelta(hours=restnd_mint) :
      worker.time_median = ((datetime.strptime(worker.starttime, '%H:%M').hour+datetime.strptime(worker.endtime, '%H:%M').hour)+((datetime.strptime(worker.starttime, '%H:%M').minute+datetime.strptime(worker.endtime, '%H:%M').minute)/60))/2
      worker.need_rest = True

  # 従業員の就業時間の中央値を用いて、営業時間の中央値に近い順に並び替える
  workers = sorted(workers,key=lambda x:abs(store_median-x.time_median))
  # print(workers_sorted)

  # 就業時間の中央値の付近から休憩の時間を見つけ出す
  restshifts = []
  for worker in workers:
    if worker.need_rest:  # 休憩が必要か
      worker.tmp_reststart = datetime.strptime(str(int(worker.time_median))+":00", '%H:%M')
      worker.tmp_restend = datetime.strptime(str(int(worker.time_median)+1)+":00", '%H:%M')
      First = True # 最初のループか
      # 休憩を入れたい時間にすでに仕事が入っている場合、休憩を他の時間に変える
      while not worker.be_free(worker.tmp_reststart,worker.tmp_restend):
        if First:
          First = False
          # 就業時間の中央値をもとに、休憩時間のずらす方向を前後に変える。
          if int(worker.time_median+0.5) == int(worker.time_median):
            worker.diffrence = -1
            worker.tmp_reststart = worker.tmp_reststart + timedelta(hours=worker.difference) 
            worker.tmp_restend = worker.tmp_restend + timedelta(hours=worker.difference) 
          else:
            worker.diffrence = 1
            worker.tmp_reststart = worker.tmp_reststart + timedelta(hours=worker.difference) 
            worker.tmp_restend = worker.tmp_restend + timedelta(hours=worker.difference) 
        else:
          # 上でずらした前後方向とは反対方向にずらす
          if not worker.done_reversed:
            worker.tmp_reststart = datetime.strptime(str(int(worker.time_median))+":00", '%H:%M')
            worker.tmp_restend = datetime.strptime(str(int(worker.time_median)+1)+":00", '%H:%M')
            worker.tmp_reststart = worker.tmp_reststart - timedelta(hours=worker.difference) 
            worker.tmp_restend = worker.tmp_restend - timedelta(hours=worker.difference) 
            worker.done_reversed = True
          # ずらす幅を大きくし動作を繰り返す
          else:
            if worker.difference > 0:
              worker.difference = worker.difference + 1
            else :
              worker.difference = worker.difference - 1
            worker.tmp_reststart = datetime.strptime(str(int(worker.time_median))+":00", '%H:%M')
            worker.tmp_restend = datetime.strptime(str(int(worker.time_median)+1)+":00", '%H:%M')
            worker.tmp_reststart = worker.tmp_reststart + timedelta(hours=worker.difference) 
            worker.tmp_restend = worker.tmp_restend + timedelta(hours=worker.difference) 
            worker.done_reversed = False
      shift = Shift(worker.workername,restname,worker.tmp_reststart,worker.tmp_restend,0)
      worker.add_shift(shift)
      restshifts.append(shift)
  # print(restshifts)
  # print(newworkers)
  return restshifts