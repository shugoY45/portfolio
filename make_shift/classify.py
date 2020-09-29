from setting import *


def Classify(Shift,IndivShift):
  # # print(Shift)

  # # 最小シフト時間に合わせて個人シフトの大きさを変更
  # pminute = int(datetime.strptime(min_shift,"%H:%M").minute) if not int(datetime.strptime(min_shift,"%H:%M").minute) == 0 else int(datetime.strptime(min_shift,"%H:%M").hour*60)
  
  # シフトに合わせて、時間ごとに個人シフトに仕事を挿入
  for shift in Shift:
    for indiv in IndivShift:
      if shift[shift_workername] == indiv[indiv_workername][0]:
        start = datetime.strptime(shift[shift_starttime],"%H:%M")
        end = datetime.strptime(shift[shift_endtime],"%H:%M")
        open_time = datetime.strptime(store_opentime,"%H:%M")
        start_num = (start.hour*60+start.minute-open_time.hour*60-open_time.minute)/pminute+1
        end_num = (end.hour*60+end.minute-open_time.hour*60-open_time.minute)/pminute+1
        for num in range(int(start_num),int(end_num)):
          indiv[num] = [shift[shift_jobname],shift[shift_weight]]

  
  # print(IndivShift)

  return IndivShift