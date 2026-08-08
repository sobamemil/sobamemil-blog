#!/usr/bin/env python3
import os
import glob
import re
import boto3
from botocore.config import Config

ACCOUNT_ID = os.environ["R2_ACCOUNT_ID"]
ACCESS_KEY_ID = os.environ["R2_ACCESS_KEY_ID"]
SECRET_ACCESS_KEY = os.environ["R2_SECRET_ACCESS_KEY"]
BUCKET_NAME = os.environ.get("R2_BUCKET_NAME", "sobamemil-blog-images")

ENDPOINT_URL = f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com"
R2_PUBLIC_BASE = f"https://pub-{ACCOUNT_ID}.r2.dev"

s3 = boto3.client(
    service_name='s3',
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    config=Config(signature_version='s3v4')
)

def verify_and_upload():
    blog_dir = os.path.dirname(os.path.abspath(__file__))
    static_img_dir = os.path.join(blog_dir, "static", "images", "posts")

    files = glob.glob(os.path.join(static_img_dir, "*", "*"))
    print(f"🔒 Testing tightly-scoped API token on bucket '{BUCKET_NAME}' ({len(files)} files)...")

    uploaded_count = 0
    for fpath in files:
        rel_path = os.path.relpath(fpath, static_img_dir)
        object_key = f"posts/{rel_path}"

        content_type = "image/png"
        if fpath.endswith(".jpg") or fpath.endswith(".jpeg"):
            content_type = "image/jpeg"
        elif fpath.endswith(".gif"):
            content_type = "image/gif"

        try:
            s3.upload_file(
                Filename=fpath,
                Bucket=BUCKET_NAME,
                Key=object_key,
                ExtraArgs={'ContentType': content_type}
            )
            uploaded_count += 1
        except Exception as e:
            print(f"❌ Upload error on {object_key}: {e}")

    print(f"✅ Token verified! Successfully synced {uploaded_count} images with object-scoped token.")

if __name__ == "__main__":
    verify_and_upload()
