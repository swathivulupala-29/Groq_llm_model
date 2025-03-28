import boto3
import streamlit as st
import os
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
load_dotenv()

# AWS credentials should be configured in ~/.aws/credentials or set as environment variables
#AWS_ACCESS_KEY = 'YOUR_ACCESS_KEY'
AWS_ACCESS_KEY = os.getenv("access_key")
#AWS_SECRET_KEY = 'YOUR_SECRET_KEY'
AWS_SECRET_KEY = os.getenv("secret_key")
#BUCKET_NAME = 'your-bucket-name'
BUCKET_NAME =os.getenv("bucket_name")
print(AWS_ACCESS_KEY, AWS_SECRET_KEY, BUCKET_NAME)
FILE_NAME = 'chat_history.txt'
S3_KEY = 'llmchat_load.txt'  # Name to save in S3

def upload_to_s3():
    try:
        # Create S3 client
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name='us-east-2'
        )
        
        # Upload file
        s3.upload_file(FILE_NAME, BUCKET_NAME, S3_KEY)
        print(f"File '{FILE_NAME}' uploaded to '{BUCKET_NAME}/{S3_KEY}'")
    
    except FileNotFoundError:
        print("The file was not found")
    except NoCredentialsError:
        print("Credentials not available")

st.title("Upload file to S3")
uploaded_file = st.file_uploader("Choose a file",type=['txt','csv','xlsx'])

if uploaded_file is not None:
    """with open(uploaded_file.name, 'wb') as f:
        f.write(uploaded_file.getbuffer())"""
    FILE_NAME = uploaded_file.name
    upload_to_s3()
    st.write(f"File uploaded to S3: {BUCKET_NAME}/{S3_KEY}")
    os.remove(uploaded_file.name)


if __name__ == "__main__":
    upload_to_s3()
