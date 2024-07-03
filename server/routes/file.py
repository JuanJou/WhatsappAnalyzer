from typing import Annotated
from fastapi import APIRouter, UploadFile, Depends, Query, Security
from services.file import validate, is_valid_uuid
import uuid


router = APIRouter(prefix="/file", tags=["file"])


def validate_file(file: UploadFile):
    return validate(file)

file_validation = Annotated[UploadFile, Depends(validate_file)]


def get_current_user(user):
    return user

@router.post("/parse")
def parse(file: file_validation, status):
    print(f"File validation: {file}")
    return {"Status": "OK", "file_name": file.filename}

@router.get("/metrics")
def get_metrics(file_id: Annotated[str, Depends(is_valid_uuid)], user: Annotated[str, Security(get_current_user, scopes=["metrics"])] ):
    print(f"File id: {file_id}")
    print(f"User id: {user}")
    return {"Status": "OK", "valid_id": file_id}
