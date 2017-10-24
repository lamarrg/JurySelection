from flask import Flask, render_template, redirect

from juror import JurorModel, jurors
from trial import TrialModel, trials
#import pdf

app = Flask(__name__)
app.register_blueprint(jurors)
app.register_blueprint(trials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'klanoiew239jpdw'


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def home():
    return redirect('/trials')


@app.route('/trials')
def trial_name():
    trial_names = TrialModel.retrieve_trials()
    return render_template('trial-list.html', trial_names=trial_names)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)

