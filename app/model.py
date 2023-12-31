from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, Date, BigInteger, DateTime, SmallInteger
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData
from config import Base
from config import engine

metadata = MetaData()


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    date_of_birth = Column(Date)
    user_info_id = Column(Integer, ForeignKey('user_info.id'))
    gender = Column(Integer)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)

    user_info = relationship("UserInfo", back_populates="user")
    snils = relationship("Snils", back_populates="user")


class UserInfo(Base):
    __tablename__ = 'user_info'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    phone = Column(Integer)
    user_type = Column(Integer)
    mail = Column(String)
    site = Column(String)

    user = relationship("User", back_populates="user_info")
    promo_info = relationship("PromoInfo", back_populates="info")


class Auth(Base):
    __tablename__ = 'auth'
    __table_args__ = {'extend_existing': True}
    login = Column(String, primary_key=True)
    password = Column(String)
    user_info_id = Column(Integer, ForeignKey('user_info.id'))


class Card(Base):
    __tablename__ = 'card'
    __table_args__ = {'extend_existing': True}
    user_id = Column(Integer, ForeignKey('users.id'))
    expire_date = Column(Date)
    card_num = Column(BigInteger, primary_key=True)


class Session(Base):
    __tablename__ = 'session'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    conductor_id = Column(Integer, ForeignKey('users.id'))
    transport_id = Column(SmallInteger, ForeignKey('transport.id'))


class Transport(Base):
    __tablename__ = 'transport'
    __table_args__ = {'extend_existing': True}
    id = Column(SmallInteger, primary_key=True)
    transport_num = Column(String)


class Snils(Base):
    __tablename__ = 'snils'
    __table_args__ = {'extend_existing': True}
    snils_num = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="snils")


class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String)

    partners = relationship("Partner", back_populates="category")


class Partner(Base):
    __tablename__ = 'partners'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    # partner_id = Column(Integer, ForeignKey('promo.promo_id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    info_id = Column(Integer, ForeignKey('promo_info.id'))
    partner_name = Column(String)

    category = relationship("Category", back_populates="partners")
    # promo = relationship("Promo", back_populates="partners")
    info = relationship("PromoInfo", back_populates="promo_info")


class Promo(Base):
    __tablename__ = 'promo'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    promo_id = Column(Integer, ForeignKey('promo_info.id'))
    partner_id = Column(Integer, ForeignKey('partners.id'))
    promo_category_id = Column(Integer, ForeignKey('promo_categories.id'))
    isactive = Column(Boolean)

    partners = relationship("Partner", back_populates="promo")
    promo_info = relationship("PromoInfo", back_populates="promo")
    promo_category = relationship("PromoCategory", back_populates="promo")


class PromoInfo(Base):
    __tablename__ = 'promo_info'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    adv = Column(Text)

    # info = relationship("UserInfo", back_populates="promo_info")
    promo = relationship("Promo", back_populates="promo_info")


class PromoCategory(Base):
    __tablename__ = 'promo_categories'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    categorie_name = Column(String)

    promo = relationship("Promo", back_populates="promo_category")
    # categories = relationship("Category", back_populates="partners")
    promo_categories = relationship("PromoCategory", back_populates="promo_category")


metadata.create_all(engine)
