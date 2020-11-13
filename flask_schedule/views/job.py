from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.forms import JobForm, SpJobForm
from flask_schedule.models import Job, Shift_config
from flask_schedule.views.login import login_required



@app.route('/job', methods=['GET', 'POST'])
@login_required
def job():
  jobs = Job.query.all()
  form = JobForm()
  config = Shift_config.query.first()
  config.init()
  form.priority.choices = config.priorty_list
  if request.method == "GET":
    return render_template('job/job.html',form=form,jobs=jobs)
  if request.method == 'POST':
    if form.validate_on_submit():
      flash('仕事を追加しました', 'success')
      job = Job(jobname=form.jobname.data, starttime=form.starttime.data, endtime=form.endtime.data, priority=form.priority.data , required_number=form.required_number.data)
      db.session.add(job)
      db.session.commit()
      jobs = Job.query.all()
      return render_template('job/job.html',form=form,jobs=jobs)

@app.route('/job/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_job(id):
  job = Job.query.get_or_404(id)
  form = JobForm()
  config = Shift_config.query.first()
  config.init()
  form.priority.choices = config.priorty_list
  if form.validate_on_submit():
    flash('編集しました', 'success')
    job.jobname = form.jobname.data
    job.starttime=form.starttime.data
    job.endtime=form.endtime.data
    job.priority = form.priority.data
    job.required_number = form.required_number.data
    db.session.commit()
    return redirect(url_for('job'))
  elif request.method == "GET":
    form.jobname.data = job.jobname
    form.starttime.data = job.starttime
    form.endtime.data = job.endtime
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