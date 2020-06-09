import boto3
import logging
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')

def download():
    logging.info("")

def upload(filename, object_name=None):
    if object_name is None:
        object_name = filename

    client = boto3.client('s3')
    try:
        for bucket in s3.buckets.all():
            if "ifolder" in bucket.name:
                logging.info(f"Found iFolder bucket on s3")
                response = client.upload_file(filename, bucket.name, object_name)
            else:
                logging.info(bucket)

    except ClientError as e:
        logging.error(f"Failed to upload: {filename} | {e}")
        return False
    else:
        logging.error("Something bad happened - and we don't know what")
    return True
    
