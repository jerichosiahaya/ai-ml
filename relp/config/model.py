from google.cloud import storage
from pathlib import Path
from config.log import log
import time

class Model:
    def __init__(self, google_credentials, bucket_name, folder_name, logger):
        self.google_app_credentials = google_credentials
        self.bucket_name = bucket_name
        self.folder_name = folder_name
        self.logging = logger

    def load_model(self) -> str:
        start_time = time.time()
        self.logging.info("Starting downloading the model from cloud storage...")
        storage_client = storage.Client.from_service_account_json(self.google_app_credentials)
        bucket = storage_client.bucket(bucket_name=self.bucket_name)
        blobs = bucket.list_blobs(prefix=self.folder_name)
        path = ""
        for blob in blobs:
            if blob.name.endswith("/"):
                continue
            file_split = blob.name.split("/")
            Path(file_split[-2]).mkdir(parents=True, exist_ok=True)
            local_file_path = Path(file_split[-2]) / file_split[-1]
            blob.download_to_filename(local_file_path)
            path = file_split[-2]
        end_time = time.time()
        self.logging.info("Time taken for downloading the model: %.2f minutes", (end_time - start_time) / 60)
        return path