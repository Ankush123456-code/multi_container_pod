from fastapi import FastAPI
from service.file_convertor import upload_router

app = FastAPI(title="main")
app.include_router(upload_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
