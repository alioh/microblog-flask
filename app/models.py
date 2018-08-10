from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True , unique= True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(120), index = True, unique = True)

    def __repr__(self):
        return '<User {}>'.format(self.username) 


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(64), nullable=False)
    post = db.Column(db.String(400))
    date_time = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return '<Post {}>'.format(self.post) 