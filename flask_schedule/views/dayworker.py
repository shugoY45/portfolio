from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.forms import DayworkerForm
from flask_schedule.models import  Shiftconfig, Dayworker ,Worker
from flask_schedule.views.login import login_required
from flask_schedule.views.views import date_chosen

@app.route('/dayworker', methods=['GET', 'POST'])
@login_required
@date_chosen
def dayworker():
  one_date = session['date']
  workers = Dayworker.query.filter_by(one_date=one_date).all()

  return render_template('dayworker/dayworker.html',workers=workers)

@app.route('/dayworker/new', methods=['GET', 'POST'])
@login_required
@date_chosen
def daynew_worker():
  one_date = session['date']
  strdate = one_date.strftime('%Y/%m/%d (%a)')
  flash(strdate+'に追加します', 'success')
  form =DayworkerForm()
  worker_list = []
  workers = Worker.query.all()
  for worker in workers:
    worker_list.append(worker.workername)
  form.workername.choices = worker_list
  if request.method == "POST":
    if form.validate_on_submit():
      flash('追加しました', 'success')
      worker = Dayworker()
      worker.one_date = one_date
      worker.workername = form.workername.data
      worker.starttime=form.starttime.data
      worker.endtime=form.endtime.data
      db.session.add(worker)
      db.session.commit()

      return redirect(url_for('dayworker'))
    else:
      return render_template('dayworker/new.html',form=form)
  elif request.method == "GET":
    return render_template('dayworker/new.html',form=form)


@app.route('/dayworker/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def dayedit_worker(id):
  worker = Dayworker.query.get_or_404(id)
  form = DayworkerForm()
  worker_list = []
  workers = Worker.query.all()
  for i in workers:
    worker_list.append(i.workername)
  form.workername.choices = worker_list
  if request.method == "POST":
    if form.validate_on_submit():
      flash('編集しました', 'success')
      worker = Dayworker()
      worker.workername = form.workername.data
      worker.starttime=form.starttime.data
      worker.endtime=form.endtime.data
      db.session.commit()
      return redirect(url_for('dayworker'))
    else:
      raise EnvironmentError("validation error")
  else:
    form.workername.data = worker.workername
    form.starttime.data = worker.starttime
    form.endtime.data = worker.endtime
    
    flash('編集します', 'warning')
    return render_template('dayworker/edit.html',form=form)

@app.route('/dayworker/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_dayworker(id):
  worker = Dayworker.query.get_or_404(id)
  if request.method == "POST":
    flash('削除しました', 'success')
    db.session.delete(worker)
    db.session.commit()
    return redirect(url_for('dayworker'))
  elif request.method == "GET":
    flash('削除しますか？', 'warning')
    return render_template('dayworker/delete.html',worker=worker)
