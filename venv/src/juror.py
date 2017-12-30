from db import db
from flask import Blueprint, request, redirect, render_template
from trial import TrialModel
import pdf

jurors = Blueprint('juror', __name__, template_folder='templates')


class JurorModel(db.Model):
    __tablename__ = 'potential_juror'

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.INTEGER)
    occupation = db.Column(db.String(120))
    details = db.Column(db.String(120))
    # trial = db.Column(db.String(80))
    foreign_key = db.Column(db.INTEGER, db.ForeignKey('trials.id'))

    def __init__(self, foreign_key, name, age, occupation, details):
        self.foreign_key = int(foreign_key)
        self.name = name
        self.age = int(age)
        self.occupation = occupation
        self.details = details

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def update_to_db():
        db.session.commit()

    def get_trial_name(self):
        trial_name = TrialModel.query.filter_by(id=self.foreign_key).first()
        return trial_name.name

    @staticmethod
    def retrieve_jurors():
        all_jurors = JurorModel.query.all()
        return all_jurors

    def remove_juror(self):
        # delete pdf file
        db.session.delete(self)
        db.session.commit()


@jurors.route('/juror/new', methods=['GET','POST'])
def add_juror():
    trial_names = TrialModel.retrieve_trials()
    if request.method == 'POST':
        foreign_key = request.form['foreign_key']
        name = request.form['name']
        age = request.form['age']
        occupation = request.form['occupation']
        details = request.form['details']
        new_juror = JurorModel(foreign_key, name, age, occupation, details)
        new_juror.save_to_db()
        pdf.print_juror(new_juror)
    return render_template('add-juror.html', trial_names=trial_names)


@jurors.route('/juror/edit/<int:num1>', methods=['GET', 'POST'])
def edit_juror(num1):
    trial_names = TrialModel.retrieve_trials()
    if request.method == 'GET':
        juror_data = JurorModel.query.filter_by(id=num1).first()
        return render_template('edit-juror.html', trial_names=trial_names, juror_data=juror_data)

    if request.method == 'POST':
        juror_edited = JurorModel.query.filter_by(id=num1).first()
        juror_edited.foreign_key = request.form['foreign_key']
        juror_edited.name = request.form['name']
        juror_edited.age = request.form['age']
        juror_edited.occupation = request.form['occupation']
        juror_edited.details = request.form['details']
        juror_edited.update_to_db()
        pdf.print_juror(juror_edited)
        print(juror_edited.age)
        return redirect('/juror/details/{}'.format(num1))


@jurors.route('/juror/delete/<int:juror_id>/<trial_id>')
def delete_juror(juror_id, trial_id):
    juror_delete = JurorModel.query.filter_by(id=juror_id).first()
    juror_delete.remove_juror()
    pdf.remove_juror_pdf(juror_delete)
    return redirect('/trial/{}'.format(trial_id))


@jurors.route('/juror/details/<int:num1>')
def juror_details(num1):
    juror = JurorModel.query.filter_by(id=num1).first()
    return render_template('/juror-details.html', juror=juror)

