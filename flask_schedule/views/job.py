from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.forms import JobForm, SpJobForm
from setting import hourlist,minuteslist, priorty_list
from flask_schedule.models import Job
from flask_schedule.views.login import login_required



@app.route('/job', methods=['GET', 'POST'])
@login_required
def job():
  jobs = Job.query.all()
  form = JobForm()
  hour = hourlist
  minutes = minuteslist
  form.starttime_hour.choices = hourlist
  form.starttime_minutes.choices = minuteslist
  form.endtime_hour.choices = hourlist
  form.endtime_minutes.choices = minuteslist
  form.priority.choices = priorty_list
  if request.method == "GET":
    return render_template('job/job.html',form=form,jobs=jobs)
  if request.method == 'POST':
    if form.validate_on_submit():
      flash('仕事を追加しました', 'success')
      job = Job(jobname=form.jobname.data, starttime=form.starttime_hour.data+':'+form.starttime_minutes.data, endtime=form.endtime_hour.data+':'+form.endtime_minutes.data, priority=form.priority.data , required_number=form.required_number.data)
      db.session.add(job)
      db.session.commit()
      jobs = Job.query.all()
      return render_template('job/job.html',form=form,jobs=jobs)

@app.route('/job/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_job(id):
  job = Job.query.get_or_404(id)
  form = JobForm()
  hour = hourlist
  minutes = minuteslist
  form.starttime_hour.choices = hourlist
  form.starttime_minutes.choices = minuteslist
  form.endtime_hour.choices = hourlist
  form.endtime_minutes.choices = minuteslist
  form.priority.choices = priorty_list
  if form.validate_on_submit():
    flash('編集しました', 'success')
    job.jobname = form.jobname.data
    job.starttime=form.starttime_hour.data+':'+form.starttime_minutes.data
    job.endtime=form.endtime_hour.data+':'+form.endtime_minutes.data
    job.priority = form.priority.data
    job.required_number = form.required_number.data
    db.session.commit()
    return redirect(url_for('job'))
  elif request.method == "GET":
    form.jobname.data = job.jobname
    form.starttime_hour.data = job.starttime.split(':')[0]
    form.starttime_minutes.data = job.starttime.split(':')[1]
    form.endtime_hour.data = job.endtime.split(':')[0]
    form.endtime_minutes.data = job.endtime.split(':')[1]
    form.priority.data = job.priority
    form.required_number.data = job.required_number
    flash('編集します', 'warning')
    return render_template('job/edit.html',form=form,job=job)


@app.route('/job/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_job(id):
  job = Job.query.get_or_404(id)
  if request.method == "POST":
    flash('削除しました', 'success')
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('job'))
  elif request.method == "GET":
    flash('削除しますか？', 'warning')
    return render_template('job/delete.html',job=job)