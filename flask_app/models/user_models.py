from flask_app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(6), nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    smoker = db.Column(db.String(3), nullable=False)

    def __repr__(self):
        return f'User id : {self.id}, User username : {self.username}, User age : {self.age}, User sex : {self.sex}, User bmi = {self.bmi}, User smoker = {self.smoker}'