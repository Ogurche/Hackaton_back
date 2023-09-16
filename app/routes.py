from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from model import User, UserInfo, Auth, Card, Transport, Snils, Session
from config import SessionLocal
from schemas import UserCreate, UserInfoCreate, AuthSchema, UserSchema, UserInfoSchema, CardSchema, SessionSchema, \
    TransportSchema, SnilsSchema
from fastapi.openapi.docs import get_swagger_ui_html
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





# User endpoints
@router.post("/users/")
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# UserInfo endpoints
@router.post("/user_info/")
async def create_user_info(user_info: UserInfoSchema, db: Session = Depends(get_db)):
    db_user_info = UserInfo(**user_info.dict())
    db.add(db_user_info)
    db.commit()
    db.refresh(db_user_info)
    return db_user_info


@router.get("/user_info/{user_info_id}")
async def read_user_info(user_info_id: int, db: Session = Depends(get_db)):
    db_user_info = db.query(UserInfo).filter(UserInfo.id == user_info_id).first()
    if not db_user_info:
        raise HTTPException(status_code=404, detail="User info not found")
    return db_user_info


# Auth endpoints
@router.post("/auth/")
async def create_auth(auth: AuthSchema, db: Session = Depends(get_db)):
    db_auth = Auth(**auth.dict())
    db.add(db_auth)
    db.commit()
    db.refresh(db_auth)
    return db_auth


@router.get("/auth/{login}")
async def read_auth(login: str, db: Session = Depends(get_db)):
    db_auth = db.query(Auth).filter(Auth.login == login).first()
    if not db_auth:
        raise HTTPException(status_code=404, detail="Auth not found")
    return db_auth


# Card endpoints
@router.post("/cards/")
async def create_card(card: CardSchema, db: Session = Depends(get_db)):
    db_card = Card(**card.dict())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


@router.get("/cards/{user_id}")
async def read_card(user_id: int, db: Session = Depends(get_db)):
    db_card = db.query(Card).filter(Card.user_id == user_id).first()
    if not db_card:
        raise HTTPException(status_code=404, detail="Card not found")
    return db_card


# Session endpoints
@router.post("/sessions/")
async def create_session(session: SessionSchema, db: Session = Depends(get_db)):
    db_session = Session(**session.dict())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session


@router.get("/sessions/{session_id}")
async def read_session(session_id: int, db: Session = Depends(get_db)):
    db_session = db.query(Session).filter(Session.id == session_id).first()
    if not db_session:
        raise HTTPException(status_code=404, detail="Session not found")
    return db_session


# Transport endpoints
@router.post("/transport/")
async def create_transport(transport: TransportSchema, db: Session = Depends(get_db)):
    db_transport = Transport(**transport.dict())
    db.add(db_transport)
    db.commit()
    db.refresh(db_transport)
    return db_transport


@router.get("/transport/{transport_id}")
async def read_transport(transport_id: int, db: Session = Depends(get_db)):
    db_transport = db.query(Transport).filter(Transport.id == transport_id).first()
    if not db_transport:
        raise HTTPException(status_code=404, detail="Transport not found")
    return db_transport


# Snils endpoints
@router.post("/snils/")
async def create_snils(snils: SnilsSchema, db: Session = Depends(get_db)):
    db_snils = Snils(**snils.dict())
    db.add(db_snils)
    db.commit()
    db.refresh(db_snils)
    return db_snils


@router.get("/snils/{snils_num}")
async def read_snils(snils_num: int, db: Session = Depends(get_db)):
    db_snils = db.query(Snils).filter(Snils.snils_num == snils_num).first()
    if not db_snils:
        raise HTTPException(status_code=404, detail="Snils not found")
    return db_snils
