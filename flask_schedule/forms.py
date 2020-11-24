from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, BooleanField
from wtforms.fields.html5 import TimeField
from wtforms.validators import DataRequired, Length
from datetime import time
# from flask_schedule.models import Shiftconfig

class config():
  store_opentime = time(hour=9)
  store_closetime = time(hour=22)

class WorkerForm(FlaskForm):
  # config = Shiftconfig.query.first()
  workername = StringField('名前',validators=[DataRequired(), Length(min=1, max=20)])

  Sun = BooleanField('日曜日',default=False)
  Sunstarttime = TimeField('始業時間',validators=None,default=config.store_opentime)
  Sunendtime = TimeField('終業時間',validators=None,default=config.store_closetime)

  Mon = BooleanField('月曜日',default=False)
  Monstarttime = TimeField('始業時間',validators=None,default=config.store_opentime)
  Monendtime = TimeField('終業時間',validators=None,default=config.store_closetime)

  Tue = BooleanField('火曜日',default=False)
  Tuestarttime = TimeField('始業時間',validators=None,default=config.store_opentime)
  Tueendtime = TimeField('終業時間',validators=None,default=config.store_closetime)

  Wed = BooleanField('水曜日',default=False)
  Wedstarttime = TimeField('始業時間',validators=None,default=config.store_opentime)
  Wedendtime = TimeField('終業時間',validators=None,default=config.store_closetime)

  Thu = BooleanField('木曜日',default=False)
  Thustarttime = TimeField('始業時間',validators=None,default=config.store_opentime)
  Thuendtime = TimeField('終業時間',validators=None,default=config.store_closetime)

  Fri = BooleanField('金曜日',default=False)
  Fristarttime = TimeField('始業時間',validators=None,default=config.store_opentime)
  Friendtime = TimeField('終業時間',validators=None,default=config.store_closetime)

  Sat = BooleanField('土曜日',default=False)
  Satstarttime = TimeField('始業時間',validators=None,default=config.store_opentime)
  Satendtime = TimeField('終業時間',validators=None,default=config.store_closetime)

  
  submit = SubmitField('送信')

class DayworkerForm(FlaskForm):
  # config = Shiftconfig.query.first()
  workername = SelectField('名前',validators=[DataRequired(), Length(min=1, max=20)])
  starttime = TimeField('始業時間',validators=None,default=config.store_opentime)
  endtime = TimeField('終業時間',validators=None,default=config.store_closetime)

  
  submit = SubmitField('送信')


class JobForm(FlaskForm):
  jobname = StringField('仕事名',validators=[DataRequired(), Length(min=1, max=20)])
  starttime = TimeField('開始時間',validators=[DataRequired()],default=config.store_opentime)
  endtime = TimeField('終了時間',validators=[DataRequired()],default=config.store_closetime)
  required_number = IntegerField('必要人数', validators=[DataRequired()],default=1)
  priority = SelectField('仕事の重要度（他の仕事と比べてどれだけ重要か）',validators=[DataRequired()],default=5)

  employee_priority = SelectField('社員優先度', validators=[DataRequired()],default=5)
  parttime_priority = SelectField('パート優先度', validators=[DataRequired()],default=5)
  helper_priority = SelectField('ヘルパー優先度', validators=[DataRequired()],default=5)
  weight = SelectField('仕事の重労度（仕事の大変さ）', validators=[DataRequired()],default=5)
  be_indispensable = BooleanField('必須')

  submit = SubmitField('送信')


class DayjobForm(FlaskForm):
  jobname = StringField('仕事名',validators=[DataRequired(), Length(min=1, max=20)])
  starttime = TimeField('開始時間',validators=[DataRequired()],default=config.store_opentime)
  endtime = TimeField('終了時間',validators=[DataRequired()],default=config.store_closetime)
  required_number = IntegerField('必要人数', validators=[DataRequired()],default=1)
  priority = SelectField('仕事の重要度',validators=[DataRequired()])

  submit = SubmitField('送信')


class SpJobForm(FlaskForm):
  workername = SelectField('指定従業員',validators=[DataRequired()])
  jobname = StringField('仕事名',validators=[DataRequired(), Length(min=1, max=20)])
  starttime = TimeField('開始時間',validators=[DataRequired()])
  endtime = TimeField('終了時間',validators=[DataRequired()])
  priority = SelectField('仕事の重要度',validators=[DataRequired()])

  submit = SubmitField('送信')

class Selectday(FlaskForm):
  weekday=SelectField('曜日',validators=[DataRequired()])
  submit = SubmitField('送信')

class ConfigForm(FlaskForm):
  store_opentime = TimeField('シフト開始時間')
  store_closetime = TimeField('シフト終了時間')
  job_divtime = TimeField('シフト交代時間')
  min_shift = TimeField('シフト最小時間')
  restnd_mint = TimeField('休憩が必要になる最小労働時間')
  resttime = TimeField('休憩時間')
  restname = StringField('休憩の名前（シフト表での実際の表記）')
  priorty_max = IntegerField('仕事重要度の最大値')
  submit = SubmitField('送信')


class ShiftForm(FlaskForm):
  workername = SelectField('名前',validators=[DataRequired()])
  starttime = TimeField('シフト開始時間',validators=None)
  endtime = TimeField('シフト終了時間',validators=None)
  submit = SubmitField('編集')


class TestForm(FlaskForm):
  # config = Shiftconfig.query.first()

  time = TimeField('a',validators=None,default=config.store_opentime)
  time2 = TimeField('a',validators=None,default=config.store_closetime)




