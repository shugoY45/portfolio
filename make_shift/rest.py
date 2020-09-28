from setting import *
# from special import Spshift, NewWorker
from datetime import datetime, timedelta


# 休憩シフト作成
def Rest(Worker,Spshift):

  # print(Worker)
  New2Worker = []
  # 休憩が必要な人のリスト作成。かつ始業時間と終業時間の平均時間を追加
  Needrest = []
  store_median = (datetime.strptime(store_opentime, '%H:%M').hour+datetime.strptime(store_closetime, '%H:%M').hour)/2
  for worker in Worker:
    if datetime.strptime(worker[work_end_time], '%H:%M')-datetime.strptime(worker[work_start_time], '%H:%M') > timedelta(hours=restnd_mint) :
      worker = list(worker)
      worker.append(((datetime.strptime(worker[work_start_time], '%H:%M').hour+datetime.strptime(worker[work_end_time], '%H:%M').hour)+((datetime.strptime(worker[work_start_time], '%H:%M').minute+datetime.strptime(worker[work_end_time], '%H:%M').minute)/60))/2)
      worker.append(store_median-worker[-1])
      Needrest.append((worker))
    else:
      New2Worker.append(worker)
  # リストの中央値を用いて、営業時間の中央値に近い順に並び替える
  Needrest_sorted = sorted(Needrest,key=lambda x:abs(x[5]))
  # print(Needrest_sorted)


  # リストの中央値の付近から休憩の時間を見つけ出す
  Restshift = []
  Tmp_restshift = []
  for needrest in Needrest_sorted:
    Tmp_restshift.append([needrest[worker_name],0,int(needrest[-2]),int(needrest[-2]+1),needrest[-2],False,0,False,needrest[work_start_time],needrest[work_end_time]])

  median = 4
  done_Rounding = 5
  difference = 6
  reverse = 7
  rework_start = 8
  rework_end = 9

  # print(Tmp_restshift)
  # その時間に特別シフトに入っていないか確認する
  for tmp in Tmp_restshift:
    found = False
    for spshift in Spshift:
      if tmp[worker_name] == spshift[shift_workername]:
        found = True
        while True:
          # a<x<b,c<y<dのときx,yが重なるのはc<b<d or c<a<d or (a<c and d<b)
          a = datetime.strptime(spshift[shift_starttime], '%H:%M')
          b = datetime.strptime(spshift[shift_endtime], '%H:%M')
          c = datetime.strptime(str(tmp[shift_starttime])+":00", '%H:%M')
          d = datetime.strptime(str(tmp[shift_endtime])+":00", '%H:%M')
          if (c<b and b<d) or (c<a and a<d) or (a<c and d<b) or a==c or b == d:
            # print(tmp)
            if not tmp[done_Rounding]:
              if int(tmp[median]+0.5) == tmp[shift_starttime]:
                # print(1)
                tmp = (tmp[shift_workername],0,tmp[shift_starttime]-1,tmp[shift_endtime]-1,tmp[median],True,-1,False,tmp[rework_start],tmp[rework_end])
                
              else:
                # print(2)
                tmp = (tmp[shift_workername],0,tmp[shift_starttime]+1,tmp[shift_endtime]+1,tmp[median],True,1,False,tmp[rework_start],tmp[rework_end])
                
            else:
              if not tmp[reverse]:
                # print(3)
                tmp = (tmp[shift_workername],0,int(tmp[median])-tmp[difference],int(tmp[median])+1-tmp[difference],tmp[median],True,tmp[difference]+1,True,tmp[rework_start],tmp[rework_end])
                
              else:
                # print(4)
                tmp = (tmp[shift_workername],0,int(tmp[median])+tmp[difference],int(tmp[median])+1+tmp[difference],tmp[median],True,tmp[difference],False,tmp[rework_start],tmp[rework_end])
          else:
            Restshift.append((tmp[shift_workername],restname,str(tmp[shift_starttime])+":00",str(tmp[shift_endtime])+":00"))
            New2Worker.append((tmp[shift_workername],tmp[rework_start],str(tmp[shift_starttime])+":00",0))
            New2Worker.append((tmp[shift_workername],str(tmp[shift_endtime])+":00",tmp[rework_end],0))
            break
    if not found:
      Restshift.append((tmp[shift_workername],restname,str(tmp[shift_starttime])+":00",str(tmp[shift_endtime])+":00"))
      New2Worker.append((tmp[shift_workername],tmp[rework_start],str(tmp[shift_starttime])+":00",0))
      New2Worker.append((tmp[shift_workername],str(tmp[shift_endtime])+":00",tmp[rework_end],0))

  # print(Restshift)
  # print(New2Worker)
  return New2Worker,Restshift




