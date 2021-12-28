from app import db

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.Enum("Male", "Female"))
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"{self.id}"

class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('users.uid'))
    name = db.Column(db.String(100))
    occurrence = db.Column(db.Enum("WEEKLY", "MONTHLY", "YEARLY", "ONETIME"))
    startDate = db.Column(db.Date, nullable=False)
    endDate = db.Column(db.Date)

    def __repr__(self):
        return f"{self.id}"

db.create_all()

'''
Sample Data for User:
{
    "name": "abhay",
    "gender": "Male",
    "email": "abc@gmail.com"
}

Sample Data for Event:
{
    "uid": 1,
    "name": "demo_event",
    "occurrence": "ONETIME",
    "startDate": "28-12-2021",
    "endDate": "30-12-2021"
}

'''