import boto3
import traceback
import os
from botocore.errorfactory import BaseClientExceptions

# Change the name of AWS resources
S3_BUCKET_NAME = "pdf"
LOCAL_S3_ENDPOINT = "http://localhost:9000"
AWS_KEY = "JIYE"
AWS_SECRET = "JIYE4EVER"


print(AWS_KEY)
print(AWS_SECRET)

s3 = boto3.client(
    "s3",
    endpoint_url=LOCAL_S3_ENDPOINT,
    aws_access_key_id=AWS_KEY,
    aws_secret_access_key=AWS_SECRET,
)
try:
    s3.create_bucket(Bucket=S3_BUCKET_NAME)
except Exception:
    pass


def generate_presigned_url(object_name: str, expiration: int = 3600) -> str:
    try:
        response = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": S3_BUCKET_NAME, "Key": object_name},
            ExpiresIn=expiration,
        )
        return response
    except Exception as e:
        traceback.print_exc(e)


def upload_object(filename: str, file) -> str:
    print(S3_BUCKET_NAME)
    if filename.endswith(".mp4"):
        s3.put_object(
            Body=file, Bucket=S3_BUCKET_NAME, Key=filename, ContentType="video/mp4"
        )
    else:
        s3.put_object(
            Body=file, Bucket=S3_BUCKET_NAME, Key=filename, ContentType="image/*"
        )
    return generate_presigned_url(filename)


def remove_object(filename: str) -> None:
    s3.delete_object(Bucket=S3_BUCKET_NAME, Key=filename)

with open("app.py", "rb") as file:
    upload_object("app.py", file)