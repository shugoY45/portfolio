from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.validators import DataRequired, Length

class WorkerForm(FlaskForm):
  workername = StringField('名前',validators=[DataRequired(), Length(min=2, max=20)])
  starttime_hour = SelectField('始業時間',validators=[DataRequired()])
  starttime_minutes = SelectField(':',validators=[DataRequired()])
  endtime_hour = SelectField('終業時間',validators=[DataRequired()])
  endtime_minutes = SelectField(':',validators=[DataRequired()])
  
  submit = SubmitField('送信')




