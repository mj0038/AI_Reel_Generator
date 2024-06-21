from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_name = "videos"

def upload_video(file_path):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=os.path.basename(file_path))
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
    return blob_client.url