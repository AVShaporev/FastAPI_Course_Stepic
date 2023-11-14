from pydantic import BaseModel


# создание модели User
class User(BaseModel):
    id: int
    name: str
