from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length

class WorkerForm(FlaskForm):
  workername = StringField('名前',validators=[DataRequired(), Length(min=1, max=20)])

  Sunday = BooleanField('日曜日',default=False)
  Sunstarttime_hour = SelectField('始業時間',validators=[DataRequired()])
  Sunstarttime_minutes = SelectField(':',validators=[DataRequired()])
  Sunendtime_hour = SelectField('終業時間',validators=[DataRequired()])
  Sunendtime_minutes = SelectField(':',validators=[DataRequired()])

  Monday = BooleanField('月曜日',default=False)
  Monstarttime_hour = SelectField('始業時間',validators=[DataRequired()])
  Monstarttime_minutes = SelectField(':',validators=[DataRequired()])
  Monendtime_hour = SelectField('終業時間',validators=[DataRequired()])
  Monendtime_minutes = SelectField(':',validators=[DataRequired()])

  Tuesday = BooleanField('火曜日',default=False)
  Tuestarttime_hour = SelectField('始業時間',validators=[DataRequired()])
  Tuestarttime_minutes = SelectField(':',validators=[DataRequired()])
  Tueendtime_hour = SelectField('終業時間',validators=[DataRequired()])
  Tueendtime_minutes = SelectField(':',validators=[DataRequired()])

  Wednesday = BooleanField('水曜日',default=False)
  Wedstarttime_hour = SelectField('始業時間',validators=[DataRequired()])
  Wedstarttime_minutes = SelectField(':',validators=[DataRequired()])
  Wedendtime_hour = SelectField('終業時間',validators=[DataRequired()])
  Wedendtime_minutes = SelectField(':',validators=[DataRequired()])

  Thursday = BooleanField('木曜日',default=False)
  Thustarttime_hour = SelectField('始業時間',validators=[DataRequired()])
  Thustarttime_minutes = SelectField(':',validators=[DataRequired()])
  Thuendtime_hour = SelectField('終業時間',validators=[DataRequired()])
  Thuendtime_minutes = SelectField(':',validators=[DataRequired()])

  Friday = BooleanField('金曜日',default=False)
  Fristarttime_hour = SelectField('始業時間',validators=[DataRequired()])
  Fristarttime_minutes = SelectField(':',validators=[DataRequired()])
  Friendtime_hour = SelectField('終業時間',validators=[DataRequired()])
  Friendtime_minutes = SelectField(':',validators=[DataRequired()])

  Saturday = BooleanField('土曜日',default=False)
  Satstarttime_hour = SelectField('始業時間',validators=[DataRequired()])
  Satstarttime_minutes = SelectField(':',validators=[DataRequired()])
  Satendtime_hour = SelectField('終業時間',validators=[DataRequired()])
  Satendtime_minutes = SelectField(':',validators=[DataRequired()])

  
  submit = SubmitField('送信')

class JobForm(FlaskForm):
  jobname = StringField('仕事名',validators=[DataRequired(), Length(min=1, max=20)])
  starttime_hour = SelectField('開始時間',validators=[DataRequired()])
  starttime_minutes = SelectField(':',validators=[DataRequired()])
  endtime_hour = SelectField('終了時間',validators=[DataRequired()])
  endtime_minutes = SelectField(':',validators=[DataRequired()])
  required_number = IntegerField('必要人数', validators=[DataRequired()],default=1)
  priority = SelectField('仕事の重要度',validators=[DataRequired()])

  submit = SubmitField('送信')


class SpJobForm(FlaskForm):
  workername = SelectField('指定従業員',validators=[DataRequired()])
  jobname = StringField('仕事名',validators=[DataRequired(), Length(min=1, max=20)])
  starttime_hour = SelectField('開始時間',validators=[DataRequired()])
  starttime_minutes = SelectField(':',validators=[DataRequired()])
  endtime_hour = SelectField('終了時間',validators=[DataRequired()])
  endtime_minutes = SelectField(':',validators=[DataRequired()])
  priority = SelectField('仕事の重要度',validators=[DataRequired()])

  submit = SubmitField('送信')






