from fastapi import FastAPI
from fastapi.responses import  FileResponse

from pydantic import BaseModel


app = FastAPI()

# создание модели Feedback
class Feedback(BaseModel):
    name: str
    message: str


#пример роута
@app.get("/")
# async def root():
#     return FileResponse('templates/index.html')
def read_root():
    return {"message": "Hello World!!!"}

# # новыйй роут
# @app.get("/custom")
# def read_custom_message():
#     return {"message": "This is a custom message!!!"}

# пример пользовательских данных (демонстрация)
fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}

# конечная точка для получения информации о пользователе
@app.get("/users/")
def read_users():
    return dict(list(fake_users.items()))

# конечная точка для получения информации о пользователе
@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {f"error: user {user_id} not found"}


@app.post("/feedback/")
def create_post(feedback: Feedback):
    return f"Thank you, {feedback.name}! Your post added!"