from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class UserSchema(BaseModel):
    id: int
    date_of_birth: str
    user_info: Optional["UserInfoSchema"]
    gender: int
    name: str
    surname: str
    patronymic: Optional[str]
    card: Optional["CardSchema"]
    session: Optional[List["SessionSchema"]]
    snils: Optional["SnilsSchema"]

    class Config:
        orm_mode = True


class UserInfoSchema(BaseModel):
    id: int
    phone: str
    user_type: int
    mail: str

    class Config:
        orm_mode = True


class UserInfoCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    city: str
    phone_number: str

    class Config:
        orm_mode = True


class AuthSchema(BaseModel):
    login: str
    password: str

    class Config:
        orm_mode = True


class CardSchema(BaseModel):
    user_id: int
    expire_date: str
    card_num: str

    class Config:
        orm_mode = True


class SessionSchema(BaseModel):
    id: int
    start_time: str
    end_time: str
    conductor_id: int
    transport_id: int

    class Config:
        orm_mode = True


class TransportSchema(BaseModel):
    id: int
    transport_num: str

    class Config:
        orm_mode = True


class SnilsSchema(BaseModel):
    snils_num: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    date_of_birth: str
    user_info_id: int
    gender: int
    name: str
    surname: str
    patronymic: Optional[str]


class UserUpdate(BaseModel):
    date_of_birth: Optional[str]
    user_info_id: Optional[int]
    gender: Optional[int]
    name: Optional[str]
    surname: Optional[str]
    patronymic: Optional[str]


class ResponseUser(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[UserSchema]


class ResponseUserList(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[List[UserSchema]]


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
