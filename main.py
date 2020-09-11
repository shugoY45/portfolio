from flask import *
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from forms import WorkerForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '5bdc41204800aae4cacd107625b60bfc'

# db = SQLAlchemy(app)

# def init_db(app):
#   db.init_app(app)
#   Migrate(app, db)


timelist = ("9:00","10:00","11:00")


@app.route("/", methods=["GET", "POST"])
def hello():
  form = WorkerForm()
  time = timelist
  return render_template("form.html", form=form, time=time)
  # return render_template("form.html")


@app.route('/send', methods=['GET', 'POST'])
def grade():
       if request.method == 'POST':
         return 'Form posted.'

if __name__ == '__main__':
  app.run(debug=True)
