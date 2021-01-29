from datetime import time,datetime,timedelta
import random
# from make_shift.normal import normal
# from make_shift.special import special
# from make_shift.rest import rest

def ave_time(time_list):
  # time_list = (datetime,datetime, ...)
  time_sum = timedelta(hours=0,minutes=0)
  # 時刻部分のみを抽出しtimedeltaを作成
  zero = datetime.combine(time_list[0],time(hour=0))
  for i in time_list:
    td = i - zero
    time_sum = time_sum + td
  
  td = time_sum/len(time_list) # 平均

  # （経過）時間[sec] -> 時分秒
  h, m, s = td.seconds//3600, (td.seconds//60)%60, td.seconds%60
  ave = datetime.combine(time_list[0],time(hour=h,minute=m,second=s))
  return ave

def make_one_shift(Shift,worker,job,starttime,endtime):
  shift = Shift(worker.workername,job.jobname,starttime,endtime,job.weight,job.priority,worker.position,job.employee_priority,job.parttime_priority,job.helper_priority,job.be_indispensable)
  return shift

# def minimize(workers,jobs,spjobs,config):

#   #山登り法を用いた最小化
#   #スケジュールの点数を格納する

#   opentime = config.store_opentime
#   closetime = config.store_closetime
#   hour_list = [i for i in range(opentime.hour,closetime.hour)]

#   spshifts = special(workers,spjobs,config,hour_list)
#   restshifts = rest(workers,config)

#   for i in range(1):
#     random.shuffle(hour_list)
#     normalshifts = normal(workers,jobs,config)
#     shifts = spshifts + restshifts + normalshifts
#     # score = evaluation(shifts,workers)

#   return minshifts

def evaluation(shifts,workers):
  #初期化
  score = 0
  one_date = shifts[0].starttime.date()

  #マッチング度の影響力を表す(0<degree<1)
  matching_degree = 0.8

  for worker in workers:
    indivscore = 0
    for shift in worker.indivshifts:
      #scoreに仕事の重みを追加する。役職のマッチング度が高いほどscoreが低くなる
      indivscore += int(shift.jobweight) * (100 - (1-matching_degree) * matching_position(shift))
    #同じ仕事が連続で入ることを防ぐ
    indivscore = indivscore * similarity(worker)
    score += indivscore
      
  # for shift in shifts:
  #   score += int(shift.jobweight)
  # print(score)
  return score

def matching_position(shift):
  #従業員の役職と仕事の役職優先度からマッチング度を作成（10 <= degree <= 100)
  degree = 10
  
  if shift.position == "社員":
    degree = int(shift.employee_priority)*10
  elif shift.position == "パート":
    degree = int(shift.parttime_priority)*10
  elif shift.position == "ヘルパー":
    degree = int(shift.helper_priority)*10

  return degree

def similarity(worker):
  #同じ仕事が連続して入っている時rateを大きくして返す(10<rate)
  shift_namelist = []
  rate = 0
  worker.indivshifts = sorted(worker.indivshifts,key=lambda x:(x.starttime))
  
  #その仕事の近くを探して連続していないか確認する。している場合はrateを増やす。
  tmp = worker.indivshifts[0]
  continuous = 0
  for shift in worker.indivshifts:
    if shift.jobname == tmp.jobname:
      if shift.starttime - tmp.endtime < timedelta(hours=1):
        rate += 1 + continuous
        continuous += 1
    else:
      continuous = 0
    tmp = shift

  rate = 10 + rate
  # print(rate)


  return rate

