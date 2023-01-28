from .S3Bucket import S3Bucket
import glob
import boto3

def getFiles(path):
    return glob.glob(path)

def getS3StorageInstance()->S3Bucket:
    s3=boto3.client("s3")
    return S3Bucket(client=s3,getFiles=getFiles)