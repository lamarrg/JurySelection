from db import db


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
        trials = TrialModel.query.all()
        return trials
