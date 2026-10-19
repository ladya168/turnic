import os
import uuid
from fastapi import UploadFile



UPLOAD_DIR = "static/uploads"

async def save_file(file: UploadFile):
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    

    server_file_path = os.path.join(UPLOAD_DIR, unique_filename)
    
    
    with open(server_file_path, "wb") as buffer:
        while content := await file.read(1024 * 1024): 
            buffer.write(content)

    return server_file_path
            