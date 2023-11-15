from fastapi import FastAPI
from fastapi.responses import  FileResponse, JSONResponse

from app.models.models import User

app = FastAPI()

# user: User = User(id=1, name="John Doe")

# 

@app.get("/")
# async def root():
#     return FileResponse('index.html')
def read_root():
    return {"message": "Hello World!!!"}

# новыйй роут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!!!"}

# @app.get("/user")
# def read_user():
#     return JSONResponse(content=user.dict())

# пример пользовательских данных (демонстрация)
fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}

# конечная точка для получения информации о пользователе
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return fake_users.get(user_id, {f"error: user with id - {user_id} not found"})