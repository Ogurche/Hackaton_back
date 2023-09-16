from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    date_of_birth = Column(Date)
    user_info = Column(Integer, ForeignKey('user_info.id'))
    gender = Column(Integer)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)

    user_info_rel = relationship("UserInfo", backref="user")


class UserInfo(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True)
    phone = Column(Integer)
    user_type = Column(Integer)
    mail = Column(String)


class Auth(Base):
    __tablename__ = 'auth'

    login = Column(String, primary_key=True)
    password = Column(String)
    user_info = Column(Integer, ForeignKey('user_info.id'))


class Card(Base):
    __tablename__ = 'card'

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    expire_date = Column(Date)
    card_num = Column(Integer)


class Session(Base):
    __tablename__ = 'session'

    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    conductor_id = Column(Integer, ForeignKey('user.id'))
    transport_id = Column(Integer, ForeignKey('transport.id'))


class Transport(Base):
    __tablename__ = 'transport'

    id = Column(Integer, primary_key=True)
    transport_num = Column(String)


class Snils(Base):
    __tablename__ = 'snils'

    snils_num = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user_rel = relationship("User", backref="snils")


