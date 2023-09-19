from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class UserSchema(BaseModel):
    id: int
    date_of_birth: str
    gender: int
    name: str
    surname: str
    patronymic: Optional[str]

    # user_info: Optional["UserInfoSchema"]
    # card: Optional["CardSchema"]
    # session: Optional[List["SessionSchema"]]
    # snils: Optional["SnilsSchema"]

    class Config:
        orm_mode = True


'''class UserInfoSchema(BaseModel):
    id: int
    phone: str
    user_type: int
    mail: str

    class Config:
        orm_mode = True
'''


class UserInfoSchema(BaseModel):
    id: int
    phone: str
    user_type: int
    mail: str
    site: str

    class Config:
        orm_mode = True


class AuthSchema(BaseModel):
    login: str
    password: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class UserRegistration(BaseModel):
    date_of_birth: str
    phone: str
    user_type: int
    mail: str
    site: str
    gender: int
    name: str
    surname: str
    patronymic: Optional[str]
    password: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    mail: str
    password: str

    class Config:
        orm_mode = True


class CardSchema(BaseModel):
    user_id: int
    expire_date: str
    card_num: int

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


# тут был UserCreate я хз где он использовался, но он дублируется
class ManCreate(BaseModel):
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


class Category(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class Partner(BaseModel):
    id: int
    partner_name: str
    category_id: int
    info_id: int
    promo_id: int

    class Config:
        orm_mode = True

class PromoInfo(BaseModel):
    id: int
    title: str
    description: str
    image_url: Optional[str]
    adv: Optional[str]

    class Config:
        orm_mode = True

class PromoCategory(BaseModel):
    id: int
    category: Category
    partner: Partner
    promo_info: PromoInfo

    class Config:
        orm_mode = True

class Promo(BaseModel):
    id: int
    promo_info: PromoInfo
    partner: Partner
    promo_category: PromoCategory
    isactive: bool

    class Config:
        orm_mode = True


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
