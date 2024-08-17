from fastapi import APIRouter, File, UploadFile
import subprocess
import posixpath

worker_router = APIRouter()


@worker_router.get("/health")
async def health_check():
    return {"message": "healthy"}


@worker_router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """Endpoint to upload a file"""
    file_content = await file.read()
    print("in worker_service")
    file_type = str(file.filename).split(".")[1]
    file_name = str(file.filename).split(".")[0]
    print("in worker",file_content)
    file_path = f"convertor/{file_name}.{file_type}"
    with open(file_path, "wb") as f:
        f.write(file_content)
    if file_type in ["docx", "doc"]:
        convert_doc_to_pdf(file_path)

    return {"filename": file.filename, "content_type": file.content_type}


def convert_doc_to_pdf(input_path):
    out_put_path = posixpath.dirname(input_path)
    print(out_put_path)
    command = [
        "C:\Program Files\LibreOffice\program\soffice.exe",
        '--headless',
        '--convert-to',
        'pdf',
        # '--outdir',
        input_path,
        "--output", out_put_path,

    ]
    print(out_put_path)
    subprocess.run(command)


# if __name__ == "__main__":
#     input_path = "C:/Users/Ankush babu/Desktop/Docker/multi_container/Bank_Account_Form.docx"
#     out_puth_path = "C:/Users/Ankush babu/Desktop/Docker/multi_container/bank.pdf"
#
#     convert_doc_to_pdf(input_path)
