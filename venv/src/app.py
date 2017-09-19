from flask import Flask, render_template, redirect, request, url_for


from juror import JurorModel
from trial import TrialModel
import pdf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'klanoiew239jpdw#@)(2d'


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


@app.route('/trial/<int:num1>')
def trial_jurors(num1):
    trial = TrialModel.query.filter_by(id=num1).first()
    juror_list = JurorModel.query.filter_by(foreign_key=num1).all()
    return render_template('juror-list.html', juror_list=juror_list, trial=trial)


@app.route('/trial/new', methods=['GET', 'POST'])
def add_trial():
    # ADD A DIRECTORY WITH TRIAL NAME TO STORE CARDS
    if request.method == 'POST':
        name = request.form['trial_name']
        new_trial = TrialModel(name)
        new_trial.save_to_db()
    return render_template('add-trial.html')


@app.route('/juror/new', methods=['GET','POST'])
def add_juror():
    trial_names = TrialModel.retrieve_trials()
    if request.method == 'POST':
        foreign_key = request.form['foreign_key']
        name = request.form['name']
        age = request.form['age']
        occupation = request.form['occupation']
        trial = TrialModel.query.filter_by(id=foreign_key).first()
        new_juror = JurorModel(foreign_key, name, age, occupation, trial.name)
        new_juror.save_to_db()
        pdf.print_juror(new_juror)
    return render_template('add-juror.html', trial_names=trial_names)


@app.route('/juror/edit/<int:num1>', methods=['GET', 'POST'])
def edit_juror(num1):
    trial_names = TrialModel.retrieve_trials()
    if request.method == 'GET':
        juror_data = JurorModel.query.filter_by(id=num1).first()
        return render_template('edit-juror.html', trial_names=trial_names, juror_data=juror_data)

    if request.method == 'POST':
        juror = JurorModel.query.filter_by(id=num1).first()
        juror.foreign_key = request.form['foreign_key']
        juror.name = request.form['name']
        juror.age = request.form['age']
        juror.occupation = request.form['occupation']
        trial = TrialModel.query.filter_by(id=juror.foreign_key).first()
        juror.trial = trial.name
        juror.update_to_db()
        pdf.print_juror(juror)
        return redirect('/juror-details/{}'.format(num1))


@app.route('/juror/delete/<int:juror_id>/<trial_id>')
def delete_juror(juror_id, trial_id):
    juror = JurorModel.query.filter_by(id=juror_id).first()
    juror.remove_juror()
    pdf.remove_juror_pdf(juror)
    return redirect('/trial/{}'.format(trial_id))


@app.route('/juror-details/<int:num1>')
def juror_details(num1):
    juror = JurorModel.query.filter_by(id=num1).first()
    return render_template('/juror-details.html', juror=juror)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)

