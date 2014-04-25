from app import app
from sqlalchemy import Column, Integer, String
from database import Base

class Car(Base):
    __tablename__='car'
    id=Column(Integer, primary_key=True)
    mfg = Column(String(200))
    model = Column(String(200))
    color=Column(String(200))
    year = Column(Integer)

    def __init__(self, mfg=None, model=None, color=None, year=None):
        self.mfg = mfg
        self.model = model
        self.color = color
        self.year = year


    def __repr(self):
        return "<Car {} {} {} {}>".format(self.mfg, self.model, self.color, self.year)
