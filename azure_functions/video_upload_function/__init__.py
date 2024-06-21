import logging
import os
from azure.storage.blob import BlobServiceClient
import azure.functions as func
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_name = "videos"

def upload_video(file):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file.filename)
    blob_client.upload_blob(file.stream)
    return blob_client.url

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    file = req.files.get('file')
    if not file:
        return func.HttpResponse(
            "Please pass a file in the form-data",
            status_code=400
        )

    video_url = upload_video(file)
    return func.HttpResponse(f"Video uploaded successfully: {video_url}", status_code=200)
