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

@app.get("/user")
def read_user():
    return JSONResponse(content=user.dict())