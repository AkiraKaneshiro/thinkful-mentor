from app import app
from sqlalchemy import Column, Integer, String, SmallInteger
from database import Base
from sqlalchemy.orm import relationship, backref

ROLE_USER = 1
ROLE_ADMIN = 0

class User(Base):
    __tablename__ = 'appusers'
    id = Column(Integer, primary_key = True)
    nickname = Column(String(64), unique = True)
    email = Column(String(120), unique = True)
    role = Column(SmallInteger, default = ROLE_USER)
   # posts = relationship('Post', backref = 'author', lazy = 'dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)