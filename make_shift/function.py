from setting import *

# 個人シフトを作成
def set_list(workers):

  # 最小シフト時間に合わせて個人シフトの大きさを変更
  # minute = int(datetime.strptime(min_shift,"%H:%M").minute) if not int(datetime.strptime(min_shift,"%H:%M").minute) == 0 else int(datetime.strptime(min_shift,"%H:%M").hour*60)
  indivshifts = [[[0,0] for j in range(int(datetime.strptime(store_closetime,"%H:%M").hour*60/pminute)+int(datetime.strptime(store_closetime,"%H:%M").minute/pminute)-int(datetime.strptime(store_opentime,"%H:%M").hour*60/pminute)-int(datetime.strptime(store_opentime,"%H:%M").minute/pminute)+1)] for i in workers]
  i = 0
  # 名前の挿入
  for worker in workers:
    indivshifts[i][0] = [worker.workername,'0']
    i += 1

  return indivshifts



# シフトに合わせて、時間ごとに個人シフトに仕事を挿入
def classify(Shift,indivshifts):
  
  for shift in Shift:
    for indiv in indivshifts:
      if shift[shift_workername] == indiv[indiv_workername][0]:
        start = datetime.strptime(shift[shift_starttime],"%H:%M")
        end = datetime.strptime(shift[shift_endtime],"%H:%M")
        open_time = datetime.strptime(store_opentime,"%H:%M")
        start_num = (start.hour*60+start.minute-open_time.hour*60-open_time.minute)/pminute+1
        end_num = (end.hour*60+end. minute-open_time.hour*60-open_time.minute)/pminute+1
        for num in range(int(start_num),int(end_num)):
          indiv[num] = [shift[shift_jobname],shift[shift_weight]]

  
  # print(indivshifts)

  return indivshifts



# 従業員のその日の仕事量を計算する
def workweight(workers,indivshifts,hour):
  
  newworkers = []
  for worker in workers:
    worker = list(worker)
    workweight = int(worker[work_weight])
    for indiv in indivshifts:
      if worker[worker_name] == indiv[indiv_workername][0]:
        for ind in indiv:
          workweight = workweight + int(ind[indiv_jobweight])
    worker[work_weight] = workweight
    newworkers.append(worker)
  # print(newworkers)

  return newworkers