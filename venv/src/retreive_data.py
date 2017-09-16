from juror import JurorModel
from trial import TrialModel


def retrieve_trials():
    trials = TrialModel.query.all()
    return trials


def retrieve_jurors():
    jurors = JurorModel.query.all()
    return jurors
