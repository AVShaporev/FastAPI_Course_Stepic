from fastapi import FastAPI
from fastapi.responses import  FileResponse

app = FastAPI()

#пример роута
@app.get("/")
async def root():
    return FileResponse('templates/index.html')