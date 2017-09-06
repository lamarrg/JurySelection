from juror import JurorModel
from trial import TrialModel


def new_trials():
    new_trial = TrialModel("Trial to end all trials")
    new_trial.save_to_db()

    new_trial = TrialModel("I pissed off JCP")
    new_trial.save_to_db()

    new_trial = TrialModel("No more of this!!! ")
    new_trial.save_to_db()

    new_trial = TrialModel("Deadpool for President")
    new_trial.save_to_db()


def new_jurors():
    new_juror = JurorModel(foreign_key=4, name="Blowhard", age=36, occupation="assassin")
    new_juror.save_to_db()

# cursor.execute("INSERT into trial (trial_name, password) VALUES ('Me VS the world', 'hella lust');")

# cursor.execute("INSERT into potential_jurors (trial_id, juror_name, occupation, age) VALUES (1, 'Carolyn Bodby', 'assasin', 36);")

# connection.commit()
# connection.close()