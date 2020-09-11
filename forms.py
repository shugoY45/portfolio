from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class WorkerForm(FlaskForm):
  workername = StringField('名前',validators=[DataRequired(), Length(min=2, max=20)])
  starttime = StringField('出勤時間',validators=[DataRequired(), Length(min=2, max=20)])
  starttime = StringField('退社時間',validators=[DataRequired(), Length(min=2, max=5)])
  submit = SubmitField('send')

