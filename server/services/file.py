from fastapi import UploadFile
import uuid
from db.models import File, FileData
from .analyzer import parse_file, parse_pickle
import boto3
import requests
from time import time


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


async def save_file_on_bucket(file_id, content):
    BUCKET_NAME = "whatsapp-convs"
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_KEY_ID = os.getenv("AWS_SECRET_KEY_ID")
    ENDPOINT = os.getenv("S3_ENDPOINT")

    print("Starting upload...")
    s3_client = boto3.resource('s3',
                   endpoint_url=ENDPOINT,
                   aws_access_key_id=AWS_ACCESS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET_KEY_ID,
                   aws_session_token=None,
                   config=boto3.session.Config(signature_version='s3v4'),
                   verify=False
                )

    s3_client.Bucket(BUCKET_NAME).put_object(Key=f"{string_from_date()}/{file_id}.pkl", Body=content)
    print("File uploaded")

async def read_file(file_id: uuid.UUID):
    BUCKET_NAME = "whatsapp-convs"
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_KEY_ID = os.getenv("AWS_SECRET_KEY_ID")
    ENDPOINT = os.getenv("S3_ENDPOINT")


    s3_client = boto3.client('s3',
                   endpoint_url=ENDPOINT,
                   aws_access_key_id=AWS_ACCESS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET_KEY_ID,
                   aws_session_token=None,
                   config=boto3.session.Config(signature_version='s3v4'),
                   verify=False
                )

    pickle_file = s3_client.download_file(Bucket=BUCKET_NAME,Filename=f"{file_id}.pkl", Key=f"{file_id}.pkl")
    return await parse_pickle(file_id)
