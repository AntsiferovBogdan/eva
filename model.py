from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    variants = db.Column(db.PickleType, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.String, nullable=False)
    age = db.Column(db.String, nullable=False)
    education = db.Column(db.String, nullable=False)
    marriage_status = db.Column(db.String, nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answers = db.Column(db.Text, nullable=False)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
    )
    question_id = db.Column(
        db.Integer,
        db.ForeignKey('question.id', ondelete='CASCADE'),
    )
    user = relationship('User', backref='answers')
    question = relationship('Question', backref='answers')
