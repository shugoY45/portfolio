
# パラメーターの設定ファイル



# シフト開始時間と終了時間
store_opentime = '9:00'
store_closetime = '22:00'

# シフトを区切る時間(hour)　この場合は一時間交代
job_divtime = 1

# シフトの最小時間
min_shift = "0:15"

# 休憩が必要になる最小労働時間
restnd_mint = 6

# 休憩時間
resttime = 1

# 休憩の名前
restname = "休憩"

# 仕事の重要度　最大値
priorty_max = 15


# Worker = [
#   ('吉田','17:00','22:00','0'),
#   ('佐々木','17:15','22:00','8'),
#   ('日置','9:00','12:00','6'),
#   ('星田','16:00','21:30','3'),
#   ('平島','16:00','21:30','3'),
#   ('赤木','9:00','18:00','3'),
#   ('宮城','13:00','22:00','3'),
#   ('瀬間','14:30','22:15','3'),
# ]
# worker_name = 0
# work_start_time = 1
# work_end_time = 2
# work_weight = 3

# Job = [
#   ('1','レジ','1','10','9:00','22:00'),
#   ('2','サッカー','2','9','10:00','22:00'),
#   ('3','食レジ応援','1','11','21:00','22:00'),
#   ('4','発注','1','6','9:00','22:00'),
#   ('5','品出し','1','5','9:00','22:00'),
#   ('6','商品整理','1','4','9:00','22:00'),
# ]
# job_id = 0
# job_name = 1
# required_number = 2
# job_weight = 3
# job_start_time = 4
# job_end_time = 5


# SpecialJob = [
#   ('1','meating','赤木','11:00','15:30','12'),
#   ('2','レジ応援','吉田','18:00','19:00','11'),
#   ('3','レジ応援','宮城','17:00','19:00','11'),

# ]
# spjob_id = 0
# spjob_name = 1
# spworker_name = 2
# spjob_start_time = 3
# spjob_end_time = 4
# spjob_weight = 5


# shift_workername = 0
# shift_jobname = 1
# shift_starttime = 2
# shift_endtime = 3
# shift_weight = 4

# indiv_workername = 0
# indiv_jobname = 0
# indiv_jobweight = 1

# formドロップダウン用の時間リスト作成
from datetime import datetime,  timedelta

td_shift = datetime.strptime(min_shift, '%H:%M')
opentime = datetime.strptime(store_opentime, '%H:%M')
closetime = datetime.strptime(store_closetime, '%H:%M')


hourlist = []
minuteslist = ["00"]

for hour in range(int(opentime.hour),int(closetime.hour)+1):
  hourlist.append(hour)

# print(td_shift.minute)
if not td_shift.minute == 0:
  if 60 % float(td_shift.minute) == 0:
    div = 60 / float(td_shift.minute)
  for minutes in range(1,int(div)):
    minuteslist.append(minutes*int(td_shift.minute))

phour = int(datetime.strptime(min_shift,"%H:%M").hour) if not int(datetime.strptime(min_shift,"%H:%M").hour) == 0 else 1

pminute = int(datetime.strptime(min_shift,"%H:%M").minute) if not int(datetime.strptime(min_shift,"%H:%M").minute) == 0 else 60

priorty_list = []
for i in range(0,priorty_max):
  priorty_list.append(i)
