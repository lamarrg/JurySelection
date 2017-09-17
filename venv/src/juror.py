from db import db


class JurorModel(db.Model):
    __tablename__ = 'potential_juror'

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.INTEGER)
    occupation = db.Column(db.String(120))
    trial = db.Column(db.String(80))
    foreign_key = db.Column(db.INTEGER, db.ForeignKey('trials.id'))

    def __init__(self, foreign_key, name, age, occupation, trial):
        self.foreign_key = int(foreign_key)
        self.name = name
        self.age = int(age)
        self.occupation = occupation
        self.trial = trial

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def update_to_db():
        db.session.commit()

    @staticmethod
    def retrieve_jurors():
        jurors = JurorModel.query.all()
        return jurors
