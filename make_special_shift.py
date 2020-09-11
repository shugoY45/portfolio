import datetime

# 開店時間と閉店時間
store_opentime = '9:00'
store_closetime = '22:00'


Worker = [
  ('吉田','17:00','22:00','0'),
  ('佐々木','17:15','22:00','8'),
  ('日置','9:00','12:00','6'),
  ('星田','16:00','21:30','3'),
  ('平島','16:00','21:30','3'),
  ('赤木','9:00','18:00','3'),
  ('宮城','13:00','22:00','3'),
  ('瀬間','14:30','22:15','3'),
]
worker_name = 0
work_start_time = 1
work_end_time = 2
work_weight = 3

Specialjob = [
  ('1','meating','赤木','12:00','12:30'),
  ('2','レジ応援','吉田','18:00','19:00'),

]
spjob_id = 0
spjob_name = 1
spwoker_name = 2
spjob_start_time = 3
spjob_end_time = 4

spshift = []
# 特別シフトの従業員を従業員リストから探索
for spjob in Specialjob:
  for worker in Worker:
    if spjob[spwoker_name] == worker[worker_name]:
      # 特別シフト作成
      starttime = datetime.datetime.strptime(spjob[spjob_start_time], '%H:%M')
      endtime = datetime.datetime.strptime(spjob[spjob_end_time], '%H:%M')
      spshift.append((worker[worker_name],spjob[spjob_name],starttime.time(),endtime.time()))
      
      # 特別シフトの時間を外し、従業員リストの仕事時間を更新する。
      Worker.append((worker[worker_name],worker[]))
      worker.clear()


print(spshift)




