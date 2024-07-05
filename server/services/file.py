from fastapi import UploadFile
import uuid
from db.models import File, FileData
from .analyzer import parse_file
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



async def save_file_on_bucket():
    BUCKET_NAME = "whatsapp-convs"
    AWS_ACCESS_KEY_ID = 'Jw0KBBTTnInkOiskepJJ'
    AWS_SECRET_KEY_ID = 'dBjOipYzMbrReI6n72E2q7vgl9XpRvzD526NxpYK'
    ENDPOINT="http://s3_emulator:9001"

    print("Starting upload")
    s3_client = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_KEY_ID,
            )
    s3_client.put_object(Key="file.py", Bucket=BUCKET_NAME, Body="some data")
    print("File uploaded")


def ping_url(url):
    try:
        start_time = time()
        response = requests.get(url)
        end_time = time()
        response_time = end_time - start_time
        if response.status_code == 200:
            print(f"URL: {url} is reachable. Response time: {response_time:.2f} seconds.")
        else:
            print(f"URL: {url} returned status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"URL: {url} is not reachable. Error: {e}")



def is_valid_ipv6_endpoint_url(endpoint_url):
    if UNSAFE_URL_CHARS.intersection(endpoint_url):
        return False
    hostname = f'[{urlparse(endpoint_url).hostname}]'
    return IPV6_ADDRZ_RE.match(hostname) is not None
