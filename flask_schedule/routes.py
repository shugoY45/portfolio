from flask import render_template, url_for, flash, redirect, request
from flask_schedule import app, db
from flask_schedule.forms import WorkerForm ,JobForm
from make_shift.setting import hourlist,minuteslist, priorty_list
from flask_schedule.models import Worker ,Job




@app.route("/", methods=["GET", "POST"])
def hello():
  form = WorkerForm()
  hour = hourlist
  minutes = minuteslist
  form.starttime_hour.choices = hourlist
  form.starttime_minutes.choices = minuteslist
  form.endtime_hour.choices = hourlist
  form.endtime_minutes.choices = minuteslist
  if request.method == 'POST':
    # print(1)
    if form.validate_on_submit():
      # print(2)
      flash('Your post has been created!', 'success')
      # print(type(form.starttime_hour.data))
      worker = Worker(workername=form.workername.data, starttime=form.starttime_hour.data+':'+form.starttime_minutes.data, endtime=form.endtime_hour.data+':'+form.endtime_minutes.data, workerweight='0')
      db.session.add(worker)
      db.session.commit()

      return redirect(url_for('worker'))
  return render_template("form.html", form=form)
  # return render_template("form.html")


@app.route('/worker', methods=['GET', 'POST'])
def worker():
  workers = Worker.query.all()
  form = WorkerForm()
  hour = hourlist
  minutes = minuteslist
  form.starttime_hour.choices = hourlist
  form.starttime_minutes.choices = minuteslist
  form.endtime_hour.choices = hourlist
  form.endtime_minutes.choices = minuteslist
  if request.method == "GET":
    return render_template('worker.html',form=form,workers=workers)
  if request.method == 'POST':
    if form.validate_on_submit():
      # flash('Your post has been created!', 'success')
      worker = Worker(workername=form.workername.data, starttime=form.starttime_hour.data+':'+form.starttime_minutes.data, endtime=form.endtime_hour.data+':'+form.endtime_minutes.data, workerweight='0')
      db.session.add(worker)
      db.session.commit()
      workers = Worker.query.all()
      return render_template('worker.html',form=form,workers=workers)

@app.route('/job', methods=['GET', 'POST'])
def job():
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
      # flash('Your post has been created!', 'success')
      job = Job(jobname=form.jobname.data, starttime=form.starttime_hour.data+':'+form.starttime_minutes.data, endtime=form.endtime_hour.data+':'+form.endtime_minutes.data, priorty=form.priorty.data , required_number=form.required_number.data)
      db.session.add(job)
      db.session.commit()
      jobs = Job.query.all()
      return render_template('job.html',form=form,jobs=jobs)

