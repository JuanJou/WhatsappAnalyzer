from fastapi import UploadFile
import uuid
from db.models import File, FileData
from .analyzer import parse_file
import boto3

def validate(file: UploadFile):
    print(f"File: {file.content_type}")

    match file.content_type:
        case "text/plain":
            return file
        case _:
            raise TypeError("File has wrong type")


def is_valid_uuid(uuid_to_test):
    try:
        # check for validity of Uuid
        uuid_obj = uuid.UUID(uuid_to_test, version=4)
    except ValueError:
        return "Invalid Uuid"
    return "Valid Uuid"

async def process_file(lines: str):
    uuid_for_file = uuid.uuid4()
    dataframe_with_lines = await parse_file(lines)
    dataframe_with_lines.to_pickle(f"{uuid_for_file}")
    await save_file_on_bucket()
    return File.write(FileData(file_id=str(uuid_for_file), user_id= 1))



async def save_file_on_bucket():
    BUCKET_NAME = "whatsapp-convs"
    AWS_ACCESS_KEY_ID = 'VPP0fkoCyBZx8YU0QTjH'
    AWS_SECRET_KEY_ID = 'iFq6k8RLJw5B0faz0cKCXeQk0w9Q8UdtaFzHuw4J'
    ENDPOINT="https://s3_emulator:9000"

    print("Starting upload")
    s3_client = boto3.client(
            "s3",
            aws_access_key_id=AWS_SECRET_KEY_ID,
            aws_secret_access_key=AWS_SECRET_KEY_ID,
            endpoint_url=ENDPOINT
            )
    s3_client.put_object(Key="file.py", Bucket=BUCKET_NAME, Body="some data")
    print("File uploaded")

