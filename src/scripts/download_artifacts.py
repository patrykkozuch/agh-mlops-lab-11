import os
import zipfile

import boto3

from sa.settings import Settings

s3 = boto3.client('s3')

def download_artifacts_from_s3(bucket_name, object, download_to):
    print(f"Downloading file from s3://{bucket_name}/{object} to {download_to}")
    with open(download_to, 'wb') as f:
        # For whatever reason, using threads here makes the download hangs
        s3.download_fileobj(bucket_name, object, f, Config=boto3.s3.transfer.TransferConfig(use_threads=False))


if __name__ == "__main__":
    settings = Settings()

    if settings.S3_BUCKET_NAME.strip() == "":
        raise ValueError("S3 Bucket Name must be specified")

    filename = os.path.basename(settings.models_zip_path)

    download_artifacts_from_s3(
        settings.S3_BUCKET_NAME,
        filename,
        settings.ARTIFACTS_PATH + filename
    )

    with zipfile.ZipFile(settings.models_zip_path, 'r') as zip_ref:
        zip_ref.extractall(settings.ARTIFACTS_PATH)
        os.unlink(settings.models_zip_path)

