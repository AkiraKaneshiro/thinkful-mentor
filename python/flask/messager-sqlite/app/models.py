from app import app, db
from sqlalchemy import Column, Integer, String

class Message(db.Model):
    __tablename__='message'
    id  =   db.Column(Integer, primary_key=True)
    txt =   db.Column(String(200))

    def __init__(self, txt=None):
        self.txt = txt

    def __repr(self):
        return "<Message {}>".format(self.txt)
