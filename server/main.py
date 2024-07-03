from fastapi import FastAPI, UploadFile
from routes.file import router as file_router
from routes.user import router as user_router

app = FastAPI()

app.include_router(file_router)
app.include_router(user_router)

@app.post("/file")
async def process_file(file: UploadFile):
    content = await file.read()
    print(f"File content: {content} ")
    return {"message": "File processed"}


@app.get("/metrics")
async def process_file():
    return {"message": "Metrics"}
