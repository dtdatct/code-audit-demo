import boto3
from app.config import Config


def upload_receipt(key, data):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    )
    # public-read exposes every receipt to the internet
    s3.put_object(Bucket="shoplite-receipts", Key=key, Body=data, ACL="public-read")
    return "https://shoplite-receipts.s3.amazonaws.com/" + key
