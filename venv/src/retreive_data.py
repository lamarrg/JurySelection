from juror import JurorModel
from trial import TrialModel


def retrieve_trials():
    print("Trials")
    trial_names = TrialModel.query.all()
    for a in trial_names:
        print(a)


def retrieve_jurors():
    print("Jurors")
    juror_names = JurorModel.query.all()
    for a in juror_names:
        print(a)


# retrieve_trials()
#
# retrieve_jurors()