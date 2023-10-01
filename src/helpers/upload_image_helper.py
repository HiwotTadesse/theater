import shutil
import uuid

from fastapi import HTTPException, UploadFile


def uploadImage(Poster: UploadFile,):
    random_name = uuid.uuid4()
    content_type = Poster.content_type
    if content_type not in ["image/jpeg", "image/png", "image/gif"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    with open(f"static/images/{random_name}.jpg", "wb" ) as buffer:
        
        shutil.copyfileobj(Poster.file, buffer)
    
    return f"static/images/{random_name}.jpg"