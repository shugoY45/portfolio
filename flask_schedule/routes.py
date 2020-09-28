from flask import *
from flask_schedule import app
from flask_schedule.forms import WorkerForm
from make_shift.setting import hourlist,minuteslist
from flask_schedule.models import Worker




@app.route("/", methods=["GET", "POST"])
def hello():
  form = WorkerForm()
  hour = hourlist
  minutes = minuteslist
  form.starttime_hour.choices = hourlist
  form.starttime_minutes.choices = minuteslist
  form.endtime_hour.choices = hourlist
  form.endtime_minutes.choices = minuteslist
  return render_template("form.html", form=form)
  # return render_template("form.html")


@app.route('/send', methods=['GET', 'POST'])
def grade():
       if request.method == 'POST':
         return 'Form posted.'