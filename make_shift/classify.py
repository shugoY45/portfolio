from setting import *
from datetime import datetime

shift_workername = 0
shift_jobname = 1
shift_starttime = 2
shift_endtime = 3

indiv_workername = 0

def Classify(Shift,Worker):
  # print(Shift)

  # 最小シフト時間に合わせて個人シフトの大きさを変更
  minute = int(datetime.strptime(min_shift,"%H:%M").minute) if not int(datetime.strptime(min_shift,"%H:%M").minute) == 0 else int(datetime.strptime(min_shift,"%H:%M").hour*60)
  # 個人シフトを作成
  IndivShift = [[0 for j in range(int(datetime.strptime(store_closetime,"%H:%M").hour*60/minute)+int(datetime.strptime(store_closetime,"%H:%M").minute/minute)-int(datetime.strptime(store_opentime,"%H:%M").hour*60/minute)-int(datetime.strptime(store_opentime,"%H:%M").minute/minute)+1)] for i in Worker]
  i = 0
  # 名前の挿入
  for worker in Worker:
    IndivShift[i][0] = worker[worker_name]
    i += 1
  # シフトに合わせて、時間ごとに個人シフトに仕事を挿入
  for shift in Shift:
    for indiv in IndivShift:
      if shift[shift_workername] == indiv[indiv_workername]:
        start = datetime.strptime(shift[shift_starttime],"%H:%M")
        end = datetime.strptime(shift[shift_endtime],"%H:%M")
        open_time = datetime.strptime(store_opentime,"%H:%M")
        start_num = (start.hour*60+start.minute-open_time.hour*60-open_time.minute)/minute+1
        end_num = (end.hour*60+end.minute-open_time.hour*60-open_time.minute)/minute+1
        for num in range(int(start_num),int(end_num)):
          indiv[num] = shift[shift_jobname]

  
  # print(IndivShift)

  return IndivShift