from fastapi import FastAPI
from fastapi.responses import  FileResponse

app = FastAPI()

#пример роута
@app.get("/")
# async def root():
#     return FileResponse('templates/index.html')
def read_root():
    return {"message": "Hello World!!!"}

# новыйй роут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!!!"}