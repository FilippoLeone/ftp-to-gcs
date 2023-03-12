from google.cloud import storage
import settings

class GCS:
    def __init__(self):
        self.storage_client = storage.Client.from_service_account_json(settings.service_account_path)
        self.bucket_name = settings.bucket_name

    def list_blobs(self) -> str:    
        allblobs = list(self.storage_client.list_blobs(self.bucket_name))
        return [blob.name for blob in allblobs]

    def upload_blob(self, gcs_destination: str, local_path: str) -> None:
        bucket = self.storage_client.bucket(self.bucket_name)
        blob = bucket.blob(gcs_destination)
        blob.upload_from_filename(local_path)
        return blob.exists()

    