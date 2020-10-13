from setting import *
# from special import spshifts, NewWorker
from datetime import datetime, timedelta
from flask_schedule.models import Shift


# 休憩シフト作成
def rest(workers,spshifts):

  # 休憩が必要な人のリスト作成。かつ始業時間と終業時間の平均時間を追加
  needrests = []
  store_median = (datetime.strptime(store_opentime, '%H:%M').hour+datetime.strptime(store_closetime, '%H:%M').hour)/2
  for worker in workers:
    if datetime.strptime(worker.endtime, '%H:%M')-datetime.strptime(worker.starttime, '%H:%M') > timedelta(hours=restnd_mint) :
      worker.time_median = ((datetime.strptime(worker.starttime, '%H:%M').hour+datetime.strptime(worker.endtime, '%H:%M').hour)+((datetime.strptime(worker.starttime, '%H:%M').minute+datetime.strptime(worker.endtime, '%H:%M').minute)/60))/2
      # worker.append(store_median-worker[-1])
      # worker.differ_store_median = store_median-worker.time_median
      # needrests.append((worker))
      worker.need_rest = True
      needrests.append(worker)
    # else:
    #   newworkers.append(worker)
  # リストの中央値を用いて、営業時間の中央値に近い順に並び替える

  workers_sorted = sorted(needrests,key=lambda x:abs(store_median-x.time_median))
  print(workers_sorted)


  # リストの中央値の付近から休憩の時間を見つけ出す
  restshifts = []
  tmp_restshifts = []
  for needrest in workers_sorted:
    tmp_restshifts.append([needrest[worker_name],0,int(needrest[-2]),int(needrest[-2]+1),needrest[-2],False,0,False,needrest.starttime,needrest.endtime])

  median = 4
  done_Rounding = 5
  difference = 6
  reverse = 7
  rework_start = 8
  rework_end = 9

  # # print(tmp_restshifts)
  # # その時間に特別シフトに入っていないか確認する
  # for tmp in tmp_restshifts:
  #   found = False
  #   for spshift in spshifts:
  #     if tmp[worker_name] == spshift[shift_workername]:
  #       found = True
  #       while True:
  #         # a<x<b,c<y<dのときx,yが重なるのはc<b<d or c<a<d or (a<c and d<b)
  #         a = datetime.strptime(spshift[shift_starttime], '%H:%M')
  #         b = datetime.strptime(spshift[shift_endtime], '%H:%M')
  #         c = datetime.strptime(str(tmp[shift_starttime])+":00", '%H:%M')
  #         d = datetime.strptime(str(tmp[shift_endtime])+":00", '%H:%M')
  #         if (c<b and b<d) or (c<a and a<d) or (a<c and d<b) or a==c or b == d:
  #           # print(tmp)
  #           if not tmp[done_Rounding]:
  #             if int(tmp[median]+0.5) == tmp[shift_starttime]:
  #               # print(1)
  #               tmp = (tmp[shift_workername],0,tmp[shift_starttime]-1,tmp[shift_endtime]-1,tmp[median],True,-1,False,tmp[rework_start],tmp[rework_end])
                
  #             else:
  #               # print(2)
  #               tmp = (tmp[shift_workername],0,tmp[shift_starttime]+1,tmp[shift_endtime]+1,tmp[median],True,1,False,tmp[rework_start],tmp[rework_end])
                
  #           else:
  #             if not tmp[reverse]:
  #               # print(3)
  #               tmp = (tmp[shift_workername],0,int(tmp[median])-tmp[difference],int(tmp[median])+1-tmp[difference],tmp[median],True,tmp[difference]+1,True,tmp[rework_start],tmp[rework_end])
                
  #             else:
  #               # print(4)
  #               tmp = (tmp[shift_workername],0,int(tmp[median])+tmp[difference],int(tmp[median])+1+tmp[difference],tmp[median],True,tmp[difference],False,tmp[rework_start],tmp[rework_end])
  #         else:
  #           restshifts.append((tmp[shift_workername],restname,str(tmp[shift_starttime])+":00",str(tmp[shift_endtime])+":00",'0'))
  #           newworkers.append((tmp[shift_workername],tmp[rework_start],str(tmp[shift_starttime])+":00",0))
  #           newworkers.append((tmp[shift_workername],str(tmp[shift_endtime])+":00",tmp[rework_end],0))
  #           break
  #   if not found:
  #     restshifts.append((tmp[shift_workername],restname,str(tmp[shift_starttime])+":00",str(tmp[shift_endtime])+":00",'0'))
  #     newworkers.append((tmp[shift_workername],tmp[rework_start],str(tmp[shift_starttime])+":00",0))
  #     newworkers.append((tmp[shift_workername],str(tmp[shift_endtime])+":00",tmp[rework_end],0))

  # # print(restshifts)
  # # print(newworkers)
  return 0,0