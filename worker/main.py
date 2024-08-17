from fastapi import FastAPI
from convertor.convertor_using_libreoffice import worker_router

app = FastAPI()
app.include_router(worker_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=7072)