from fastapi import APIRouter, File, UploadFile
import requests

upload_router = APIRouter()
worker_service = "http://127.0.0.1:7072/upload/"


@upload_router.get("/health")
async def health_check():
    return {"message": "healthy"}


@upload_router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """Endpoint to upload a file"""
    file_content = await file.read()
    file_type = str(file.filename).split(".")[1]
    file_name = str(file.filename).split(".")[0]
    print("file in main service", file)
    file_path = f"service/{file_name}.{file_type}"
    with open(file_path, "wb") as f:
        f.write(file_content)
    if file_type in ["docx", "doc", "pdf"]:
        files = {"file": (file.filename, file_content, file.content_type)}
        response = requests.post(worker_service, files=files)
        return {"filename": file.filename, "content_type": file.content_type, "contest": response.content,
                "status_of internal container": response.status_code}
    return {"message": "fail"}
