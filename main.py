from fastapi import FastAPI
from fastapi.responses import  FileResponse

app = FastAPI()

@app.get("/")
# async def root():
#     return FileResponse('index.html')
def read_root():
    return {"message": "Hello World!!!"}

# новыйй роут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!!!"}