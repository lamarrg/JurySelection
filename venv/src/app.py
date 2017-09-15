from flask import Flask, render_template, redirect, request, url_for


from juror import JurorModel
from trial import TrialModel
import print_pdf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'klanoiew239jpdw#@)(2d'


@app.before_first_request
def create_tables():
    db.create_all()
    import insert_data
    # insert_data.new_jurors()
    # insert_data.new_trials()


def get_nav_menu():
    return TrialModel.query.all()


def retrieve_trials():
    print("Trials")
    trial_names = TrialModel.query.all()
    for a in trial_names:
        print("{}/{}".format(a.name,a.id))


def retrieve_jurors():
    print("Jurors")
    juror_names = JurorModel.query.all()
    for a in juror_names:
        print("{}/{}".format(a.name,a.foreign_key))

@app.route('/')
def home():
    # db.session.add(justice)
    # db.session.commit()
    # return "hmmmmmm...."
    nav_menu = get_nav_menu()
    trial_names = TrialModel.query.all()
    return redirect('/trials')


@app.route('/trials')
def trial_name():
    nav_menu = get_nav_menu()
    trial_names = TrialModel.query.all()
    return render_template('trial-list.html', nav_menu=nav_menu, trial_names=trial_names)


@app.route('/trial/<int:num1>')
def trial_jurors(num1):
    trial = TrialModel.query.filter_by(id=num1).first()
    juror_list = JurorModel.query.filter_by(foreign_key=num1).all()
    nav_menu = get_nav_menu()
    return render_template('juror-list.html', juror_list=juror_list, trial=trial, nav_menu=nav_menu)


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
    trial_names = TrialModel.query.all()
    if request.method == 'POST':
        foreign_key = request.form['foreign_key']
        name = request.form['name']
        age = request.form['age']
        occupation = request.form['occupation']
        trial = TrialModel.query.filter_by(id=foreign_key).first()
        new_juror = JurorModel(foreign_key, name, age, occupation, trial.name)
        new_juror.save_to_db()

    return render_template('add-juror.html', trial_names=trial_names)

@app.route('/juror/edit/<int:num1>', methods=['GET', 'POST'])
def edit_juror(num1):
    trial_names = TrialModel.query.all()
    if request.method == 'GET':
        juror_data = JurorModel.query.filter_by(id=num1).first()
        # foreign_key = request.form['foreign_key']
        # name = request.form['name']
        # age = request.form['age']
        # occupation = request.form['occupation']
        # trial = TrialModel.query.filter_by(id=foreign_key).first()
        # juror = JurorModel(foreign_key, name, age, occupation, trial.name)
        # juror.save_to_db()
        return render_template('edit-juror.html', trial_names=trial_names, juror_data=juror_data)

    if request.method == 'POST':
        juror = JurorModel.query.filter_by(id=num1).first()
        juror.foreign_key = request.form['foreign_key']
        juror.name = request.form['name']
        juror.age = request.form['age']
        juror.occupation = request.form['occupation']
        trial = TrialModel.query.filter_by(id=juror.foreign_key).first()
        #juror = JurorModel(foreign_key, name, age, occupation, trial.name)
        juror.update_to_db()
        #juror.save_to_db()
        return redirect('/juror-details/{}'.format(num1))


@app.route('/juror-details/<int:num1>')
@app.route('/juror-details/<int:num1>/<pdf>')
def juror_details(num1, pdf=""):
    juror = JurorModel.query.filter_by(id=num1).first()
    nav_menu = get_nav_menu()
    if pdf == 'pdf':
        print(juror.name)
        print_pdf.print_juror(filename=juror.name, content=(juror.name, juror.occupation, juror.trial))
        return redirect('/juror-details/{}'.format(num1))
    return render_template('/juror-details.html', juror=juror, nav_menu=nav_menu)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)

