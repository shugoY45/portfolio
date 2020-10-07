from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.forms import WorkerForm ,JobForm
from make_shift.setting import hourlist,minuteslist, priorty_list
from flask_schedule.models import Worker ,Job


@app.route("/", methods=["GET", "POST"])
def index():
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  return render_template("index.html")


@app.route('/job', methods=['GET', 'POST'])
def job():
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  jobs = Job.query.all()
  form = JobForm()
  hour = hourlist
  minutes = minuteslist
  form.starttime_hour.choices = hourlist
  form.starttime_minutes.choices = minuteslist
  form.endtime_hour.choices = hourlist
  form.endtime_minutes.choices = minuteslist
  form.priorty.choices = priorty_list
  if request.method == "GET":
    return render_template('job.html',form=form,jobs=jobs)
  if request.method == 'POST':
    if form.validate_on_submit():
      flash('仕事を追加しました', 'success')
      job = Job(jobname=form.jobname.data, starttime=form.starttime_hour.data+':'+form.starttime_minutes.data, endtime=form.endtime_hour.data+':'+form.endtime_minutes.data, priorty=form.priorty.data , required_number=form.required_number.data)
      db.session.add(job)
      db.session.commit()
      jobs = Job.query.all()
      return render_template('job.html',form=form,jobs=jobs)

