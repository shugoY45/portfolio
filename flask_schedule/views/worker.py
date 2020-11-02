from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.forms import WorkerForm 
from setting import hourlist,minuteslist
from flask_schedule.models import Worker
from flask_schedule.views.login import login_required

@app.route('/worker', methods=['GET', 'POST'])
@login_required
def worker():
  workers = Worker.query.all()
  for worker in workers:
    print(worker.Wedstarttime)
  return render_template('worker/worker.html',workers=workers)

@app.route('/worker/new', methods=['GET', 'POST'])
@login_required
def new_worker():
  form = make_checklist(WorkerForm())
  if request.method == "POST":
    if form.validate_on_submit():
      flash('追加しました', 'success')
      Sun = request.form.get("Sun")
      Mon = request.form.get("Mon")
      Tue = request.form.get("Tue")
      Wed = request.form.get("Wed")
      Thu = request.form.get("Thu")
      Fri = request.form.get("Fri")
      Sat = request.form.get("Sat")

      worker = Worker()
      worker.workername = form.workername.data
      if Sun:
        worker.Sunday = True
      else :
        worker.Sunday = False
      worker.Sunstarttime=form.Sunstarttime_hour.data+':'+form.Sunstarttime_minutes.data
      worker.Sunendtime=form.Sunendtime_hour.data+':'+form.Sunendtime_minutes.data

      if Mon:
        worker.Monday = True
      else :
        worker.Monday = False
      worker.Monstarttime=form.Monstarttime_hour.data+':'+form.Monstarttime_minutes.data
      worker.Monendtime=form.Monendtime_hour.data+':'+form.Monendtime_minutes.data

      if Tue:
        worker.Tuesday = True
      else :
        worker.Tuesday = False
      worker.Tuestarttime=form.Tuestarttime_hour.data+':'+form.Tuestarttime_minutes.data
      worker.Tueendtime=form.Tueendtime_hour.data+':'+form.Tueendtime_minutes.data

      if Wed:
        worker.Wednesday = True
      else :
        worker.Wednesday = False
      worker.Wedstarttime=form.Wedstarttime_hour.data+':'+form.Wedstarttime_minutes.data
      worker.Wedendtime=form.Wedendtime_hour.data+':'+form.Wedendtime_minutes.data

      if Thu:
        worker.Thursday = True
      else :
        worker.Thursday = False
      worker.Thustarttime=form.Thustarttime_hour.data+':'+form.Thustarttime_minutes.data
      worker.Thuendtime=form.Thuendtime_hour.data+':'+form.Thuendtime_minutes.data

      if Fri:
        worker.Friday = True
      else :
        worker.Friday = False
      worker.Fristarttime=form.Fristarttime_hour.data+':'+form.Fristarttime_minutes.data
      worker.Friendtime=form.Friendtime_hour.data+':'+form.Friendtime_minutes.data

      if Sat:
        worker.Saturday = True
      else :
        worker.Saturday = False
      worker.Satstarttime=form.Satstarttime_hour.data+':'+form.Satstarttime_minutes.data
      worker.Satendtime=form.Satendtime_hour.data+':'+form.Satendtime_minutes.data
      db.session.add(worker)
      db.session.commit()

      # days = request.form.getlist("day")

      # worker = Worker()
      # worker.workername = form.workername.data

      # for day in days:
      #   weekday = Weekday()
      #   weekday.weekday = day

      return redirect(url_for('worker'))
    else:
      return render_template('worker/new.html',form=form)
  elif request.method == "GET":
    return render_template('worker/new.html',form=form)



@app.route('/worker/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_worker(id):
  worker = Worker.query.get_or_404(id)
  form = WorkerForm()
  form.starttime_hour.choices = hourlist
  form.starttime_minutes.choices = minuteslist
  form.endtime_hour.choices = hourlist
  form.endtime_minutes.choices = minuteslist
  if form.validate_on_submit():
    flash('編集しました', 'success')
    worker.workername = form.workername.data
    worker.starttime=form.starttime_hour.data+':'+form.starttime_minutes.data
    worker.endtime=form.endtime_hour.data+':'+form.endtime_minutes.data
    db.session.commit()
    return redirect(url_for('worker'))
  elif request.method == "GET":
    form.workername.data = worker.workername
    form.starttime_hour.data = worker.starttime.split(':')[0]
    form.starttime_minutes.data = worker.starttime.split(':')[1]
    form.endtime_hour.data = worker.endtime.split(':')[0]
    form.endtime_minutes.data = worker.endtime.split(':')[1]
    flash('編集します', 'warning')
    return render_template('worker/edit.html',form=form,worker=worker)


@app.route('/worker/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_worker(id):
  worker = Worker.query.get_or_404(id)
  if request.method == "POST":
    flash('削除しました', 'success')
    db.session.delete(worker)
    db.session.commit()
    return redirect(url_for('worker'))
  elif request.method == "GET":
    flash('削除しますか？', 'warning')
    return render_template('worker/delete.html',worker=worker)

def make_checklist(form):

  form.Monstarttime_hour.choices = hourlist
  form.Monstarttime_minutes.choices = minuteslist
  form.Monendtime_hour.choices = hourlist
  form.Monendtime_minutes.choices = minuteslist

  form.Tuestarttime_hour.choices = hourlist
  form.Tuestarttime_minutes.choices = minuteslist
  form.Tueendtime_hour.choices = hourlist
  form.Tueendtime_minutes.choices = minuteslist

  form.Wedstarttime_hour.choices = hourlist
  form.Wedstarttime_minutes.choices = minuteslist
  form.Wedendtime_hour.choices = hourlist
  form.Wedendtime_minutes.choices = minuteslist

  form.Thustarttime_hour.choices = hourlist
  form.Thustarttime_minutes.choices = minuteslist
  form.Thuendtime_hour.choices = hourlist
  form.Thuendtime_minutes.choices = minuteslist

  form.Fristarttime_hour.choices = hourlist
  form.Fristarttime_minutes.choices = minuteslist
  form.Friendtime_hour.choices = hourlist
  form.Friendtime_minutes.choices = minuteslist

  form.Satstarttime_hour.choices = hourlist
  form.Satstarttime_minutes.choices = minuteslist
  form.Satendtime_hour.choices = hourlist
  form.Satendtime_minutes.choices = minuteslist

  form.Sunstarttime_hour.choices = hourlist
  form.Sunstarttime_minutes.choices = minuteslist
  form.Sunendtime_hour.choices = hourlist
  form.Sunendtime_minutes.choices = minuteslist

  return form