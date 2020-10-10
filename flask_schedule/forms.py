from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length

class WorkerForm(FlaskForm):
  workername = StringField('名前',validators=[DataRequired(), Length(min=2, max=20)])
  starttime_hour = SelectField('始業時間',validators=[DataRequired()])
  starttime_minutes = SelectField(':',validators=[DataRequired()])
  endtime_hour = SelectField('終業時間',validators=[DataRequired()])
  endtime_minutes = SelectField(':',validators=[DataRequired()])
  
  submit = SubmitField('追加')

class JobForm(FlaskForm):
  jobname = StringField('仕事時間',validators=[DataRequired(), Length(min=1, max=20)])
  starttime_hour = SelectField('開始時間',validators=[DataRequired()])
  starttime_minutes = SelectField(':',validators=[DataRequired()])
  endtime_hour = SelectField('終了時間',validators=[DataRequired()])
  endtime_minutes = SelectField(':',validators=[DataRequired()])
  required_number = IntegerField('必要人数', validators=[DataRequired()])
  priorty = SelectField('仕事の重要度',validators=[DataRequired()])

  submit = SubmitField('追加')


class SpJobForm(JobForm):
  workername = StringField('指定従業員',validators=[DataRequired(), Length(min=2, max=20)])






