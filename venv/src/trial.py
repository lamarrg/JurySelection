from db import db
from flask import Blueprint, request, render_template



trials = Blueprint('trial', __name__, template_folder='templates')


class TrialModel(db.Model):
    __tablename__ = 'trials'

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def retrieve_trials():
        trial_list = TrialModel.query.all()
        return trial_list

    def remove_trial(self):
        # need to delete database record, folder and jurors in folder if not empty
        db.session.delete(self)
        db.session.commit()


@trials.route('/trial/<int:num1>')
def trial_jurors(num1):
    from juror import JurorModel
    juror_list = JurorModel.query.filter_by(foreign_key=num1).all()
    trial = TrialModel.query.filter_by(id=num1).first()
    return render_template('juror-list.html', juror_list=juror_list, trial=trial)


@trials.route('/trial/new', methods=['GET', 'POST'])
def add_trial():
    # ADD A DIRECTORY WITH TRIAL NAME TO STORE CARDS
    if request.method == 'POST':
        name = request.form['trial_name']
        new_trial = TrialModel(name)
        new_trial.save_to_db()
    return render_template('add-trial.html')
