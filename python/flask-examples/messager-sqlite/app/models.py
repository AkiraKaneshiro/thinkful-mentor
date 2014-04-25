from sqlalchemy import Column, Integer, String
from database import Base

class Message(Base):
    __tablename__='message'
    id=Column(Integer, primary_key=True)
    txt = Column(String(200))

    def __init__(self, txt=None):
        self.txt = txt

    def __repr(self):
        return "<Message {}".format(self.txt)
