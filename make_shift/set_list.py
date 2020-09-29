from setting import *
# from datetime import datetime


def Set_list(Worker):

  # 最小シフト時間に合わせて個人シフトの大きさを変更
  # minute = int(datetime.strptime(min_shift,"%H:%M").minute) if not int(datetime.strptime(min_shift,"%H:%M").minute) == 0 else int(datetime.strptime(min_shift,"%H:%M").hour*60)
  # 個人シフトを作成
  IndivShift = [[0 for j in range(int(datetime.strptime(store_closetime,"%H:%M").hour*60/pminute)+int(datetime.strptime(store_closetime,"%H:%M").minute/pminute)-int(datetime.strptime(store_opentime,"%H:%M").hour*60/pminute)-int(datetime.strptime(store_opentime,"%H:%M").minute/pminute)+1)] for i in Worker]
  i = 0
  # 名前の挿入
  for worker in Worker:
    IndivShift[i][0] = [worker[worker_name],'0']
    i += 1

  return IndivShift