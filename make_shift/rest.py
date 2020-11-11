from datetime import datetime, timedelta, time
from flask_schedule.models import Shift
from make_shift.function import ave_time


# 休憩シフト作成
def rest(workers,config):

  # 休憩が必要な人を探し、かつ始業時間と終業時間の平均時間を追加
  time_list = [config.store_opentime,config.store_closetime]
  store_median = ave_time(time_list)
  for worker in workers:
    if worker.endtime - worker.starttime > timedelta(hours=config.restnd_mint.hour) :
      time_list = [worker.starttime,worker.endtime]
      worker.time_median = ave_time(time_list)
      worker.need_rest = True

  # 従業員の就業時間の中央値を用いて、営業時間の中央値に近い順に並び替える
  workers = sorted(workers,key=lambda x:abs(store_median-x.time_median))
  # print(workers_sorted)

  # 就業時間の中央値の付近から休憩の時間を見つけ出す
  restshifts = []
  for worker in workers:
    if worker.need_rest:  # 休憩が必要か
      # worker.tmp_reststart = datetime.strptime(str(int(worker.time_median))+":00", '%H:%M')
      # worker.tmp_restend = datetime.strptime(str(int(worker.time_median)+1)+":00", '%H:%M')
      worker.tmp_reststart = datetime.combine(worker.time_median,time(hour=worker.time_median.hour,minute=0))
      worker.tmp_restend = datetime.combine(worker.time_median,time(hour=worker.time_median.hour+1,minute=0))
      First = True # 最初のループか
      # 休憩を入れたい時間にすでに仕事が入っている場合、休憩を他の時間に変える
      while not worker.be_free(worker.tmp_reststart,worker.tmp_restend):
        if First:
          First = False
          # 就業時間の中央値をもとに、休憩時間のずらす方向を前後に変える。
          if worker.time_median.minute <30:
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
            worker.tmp_reststart = datetime.combine(worker.time_median,time(hour=worker.time_median.hour,minute=0))
            worker.tmp_restend = datetime.combine(worker.time_median,time(hour=worker.time_median.hour+1,minute=0))
            worker.tmp_reststart = worker.tmp_reststart - timedelta(hours=worker.difference) 
            worker.tmp_restend = worker.tmp_restend - timedelta(hours=worker.difference) 
            worker.done_reversed = True
          # ずらす幅を大きくし動作を繰り返す
          else:
            if worker.difference > 0:
              worker.difference = worker.difference + 1
            else :
              worker.difference = worker.difference - 1
            worker.tmp_reststart = datetime.combine(worker.time_median,time(hour=worker.time_median.hour,minute=0))
            worker.tmp_restend = datetime.combine(worker.time_median,time(hour=worker.time_median.hour+1,minute=0))
            worker.tmp_reststart = worker.tmp_reststart + timedelta(hours=worker.difference) 
            worker.tmp_restend = worker.tmp_restend + timedelta(hours=worker.difference) 
            worker.done_reversed = False
      shift = Shift(worker.workername,config.restname,worker.tmp_reststart,worker.tmp_restend,0)
      worker.add_shift(shift)
      restshifts.append(shift)
  # print(restshifts)
  # print(newworkers)
  return restshifts