from pydantic import BaseModel


# создание модели User
class User(BaseModel):
    id: int
    name: str


# создание модели UserCreate
class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    is_subscribed: bool = None


# создание модели Feedback
class Feedback(BaseModel):
    name: str
    message: str
