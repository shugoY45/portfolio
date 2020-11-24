from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.forms import JobForm, SpJobForm
from flask_schedule.models import Job, Shiftconfig
from flask_schedule.views.login import login_required



@app.route('/job', methods=['GET', 'POST'])
@login_required
def job():
  jobs = Job.query.all()
  return render_template('job/job.html',jobs=jobs)

@app.route('/job/new', methods=['GET', 'POST'])
@login_required
def new_job():
  form = JobForm()
  config = Shiftconfig.query.first()
  config.init()
  numlist = [i for i in range(1,11)]
  form.priority.choices = numlist
  form.weight.choices = numlist
  form.employee_priority.choices = numlist
  form.parttime_priority.choices = numlist
  form.helper_priority.choices = numlist

  if request.method == 'POST':
    flash('仕事を追加しました', 'success')
    job = Job(jobname=form.jobname.data, starttime=form.starttime.data, endtime=form.endtime.data, priority=form.priority.data , required_number=form.required_number.data, weight=form.weight.data, employee_priority=form.employee_priority.data, parttime_priority=form.parttime_priority.data,helper_priority=form.helper_priority.data)
    db.session.add(job)
    db.session.commit()
    return redirect(url_for("job"))

  flash('仕事を追加します', 'success')
  return render_template('job/new.html',form=form)

@app.route('/job/<int:id>/detail', methods=['GET', 'POST'])
@login_required
def detail_job(id):
  job = Job.query.get_or_404(id)
  
  return render_template('job/detail.html',job=job)

@app.route('/job/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_job(id):
  job = Job.query.get_or_404(id)
  form = JobForm()
  config = Shiftconfig.query.first()
  config.init()
  numlist = [i for i in range(1,11)]
  form.priority.choices = numlist
  form.weight.choices = numlist
  form.employee_priority.choices = numlist
  form.parttime_priority.choices = numlist
  form.helper_priority.choices = numlist
  if request.method == "POST":
    flash('編集しました', 'success')
    job.jobname = form.jobname.data
    job.starttime=form.starttime.data
    job.endtime=form.endtime.data
    job.priority = form.priority.data
    job.required_number = form.required_number.data
    job.weight=form.weight.data
    job.employee_priority=form.employee_priority.data
    job.parttime_priority=form.parttime_priority.data
    job.helper_priority=form.helper_priority.data
    db.session.commit()
    return redirect(url_for('job'))
 
  form.jobname.data = job.jobname
  form.starttime.data = job.starttime
  form.endtime.data = job.endtime
  form.priority.data = job.priority
  form.required_number.data = job.required_number
  form.weight.data = job.weight
  form.employee_priority.data = job.employee_priority
  form.parttime_priority.data = job.parttime_priority
  form.helper_priority.data = job.helper_priority
  # print(form.weight.data)
  flash('編集します', 'warning')
  return render_template('job/edit.html',form=form)


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