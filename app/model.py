from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

from config import engine

Base = declarative_base()
metadata = MetaData()

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    date_of_birth = Column(Date)
    user_info = Column(Integer, ForeignKey('public.user_info.id'))
    gender = Column(Integer)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)

    user_info_rel = relationship("UserInfo", backref="user")


class UserInfo(Base):
    __tablename__ = 'user_info'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    phone = Column(Integer)
    user_type = Column(Integer)
    mail = Column(String)
    site = Column(String)


class Auth(Base):
    __tablename__ = 'auth'
    __table_args__ = {'schema': 'public'}

    login = Column(String, primary_key=True)
    password = Column(String)
    user_info = Column(Integer, ForeignKey('public.user_info.id'))


class Card(Base):
    __tablename__ = 'card'
    __table_args__ = {'schema': 'public'}

    user_id = Column(Integer, ForeignKey('public.user.id'))
    expire_date = Column(Date)
    card_num = Column(Integer, primary_key=True)


class Session(Base):
    __tablename__ = 'session'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    conductor_id = Column(Integer, ForeignKey('public.user.id'))
    transport_id = Column(Integer, ForeignKey('public.transport.id'))


class Transport(Base):
    __tablename__ = 'transport'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    transport_num = Column(String)


class Snils(Base):
    __tablename__ = 'snils'
    __table_args__ = {'schema': 'public'}

    snils_num = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('public.user.id'))

    user_rel = relationship("User", backref="snils")


metadata.create_all(engine)