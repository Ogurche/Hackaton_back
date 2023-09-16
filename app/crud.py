from typing import List
from sqlalchemy.orm import Session
import model
import schemas


# CRUD операции для модели User
def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = model.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(model.User).filter(model.User.id == user_id).first()
    if db_user:
        update_data = user.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(model.User).filter(model.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


# CRUD операции для модели UserInfo
def get_user_info(db: Session, user_id: int):
    return db.query(model.UserInfo).filter(model.UserInfo.user_id == user_id).first()


def create_user_info(db: Session, user_info: schemas.UserInfoCreate, user_id: int):
    db_user_info = model.UserInfo(**user_info.dict(), user_id=user_id)
    db.add(db_user_info)
    db.commit()
    db.refresh(db_user_info)
    return db_user_info


def update_user_info(db: Session, user_id: int, user_info: schemas.UserInfoSchema):
    db_user_info = db.query(model.UserInfo).filter(model.UserInfo.user_id == user_id).first()
    if db_user_info:
        update_data = user_info.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_user_info, key, value)
        db.commit()
        db.refresh(db_user_info)
    return db_user_info


# CRUD операции для модели Auth
def get_auth(db: Session, username: str):
    return db.query(model.Auth).filter(model.Auth.username == username).first()


def create_auth(db: Session, auth: schemas.AuthSchema):
    db_auth = model.Auth(**auth.dict())
    db.add(db_auth)
    db.commit()
    db.refresh(db_auth)
    return db_auth


# CRUD операции для модели Card
def get_card(db: Session, card_number: str):
    return db.query(model.Card).filter(model.Card.card_number == card_number).first()


def create_card(db: Session, card: schemas.CardSchema):
    db_card = model.Card(**card.dict())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


# CRUD операции для модели Session
def get_session(db: Session, session_id: str):
    return db.query(Session).filter(Session.session_id == session_id).first()


def create_session(db: Session, session: schemas.SessionSchema):
    db_session = Session(**session.dict())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session


def delete_session(db: Session, session_id: str):
    db_session = db.query(Session).filter(Session.session_id == session_id).first()
    if db_session:
        db.delete(db_session)
        db.commit()
    return db_session


# CRUD операции для модели Transport
def get_transport(db: Session, transport_id: int):
    return db.query(model.Transport).filter(model.Transport.id == transport_id).first()


def get_transports(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Transport).offset(skip).limit(limit).all()


def create_transport(db: Session, transport: schemas.TransportSchema):
    db_transport = model.Transport(**transport.dict())
    db.add(db_transport)
    db.commit()
    db.refresh(db_transport)
    return db_transport


def update_transport(db: Session, transport_id: int, transport: schemas.TransportSchema):
    db_transport = db.query(model.Transport).filter(model.Transport.id == transport_id).first()
    if db_transport:
        update_data = transport.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_transport, key, value)
        db.commit()
        db.refresh(db_transport)
    return db_transport


def delete_transport(db: Session, transport_id: int):
    db_transport = db.query(model.Transport).filter(model.Transport.id == transport_id).first()
    if db_transport:
        db.delete(db_transport)
        db.commit()
    return db_transport


# CRUD операции для модели Snils
def get_snils(db: Session, snils_number: str):
    return db.query(model.Snils).filter(model.Snils.snils_number == snils_number).first()


def create_snils(db: Session, snils: schemas.SnilsSchema):
    db_snils = model.Snils(**snils.dict())
    db.add(db_snils)
    db.commit()
    db.refresh(db_snils)
    return db_snils
