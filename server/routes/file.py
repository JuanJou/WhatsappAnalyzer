from typing import Annotated
from fastapi import APIRouter, UploadFile, File, Depends, Query, Security
from services.file import validate, is_valid_uuid, process_file
import uuid


router = APIRouter(prefix="/file", tags=["file"])


def validate_file(file: UploadFile):
    return validate(file)

file_validation = Annotated[UploadFile, Depends(validate_file)]


def get_current_user(user):
    return user

@router.post("/parse")
async def parse(file: bytes = File(...)):
    dataframe = await process_file(file.decode("utf-8"))
    return {"Status": "parsed"}

@router.get("/metrics")
def get_metrics(file_id: Annotated[str, Depends(is_valid_uuid)]):
    print(f"File id: {file_id}")
    print(f"User id: {user}")
    return {"Status": "OK", "valid_id": file_id}
