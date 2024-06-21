from azure.cosmos import CosmosClient, PartitionKey
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

connection_string = os.getenv("AZURE_COSMOS_CONNECTION_STRING")
client = CosmosClient.from_connection_string(connection_string)
database_name = "VideoMetadataDB"
container_name = "MetadataContainer"
database = client.create_database_if_not_exists(id=database_name)
container = database.create_container_if_not_exists(id=container_name, partition_key=PartitionKey(path="/id"))

def store_metadata(metadata):
    container.create_item(body=metadata)

def query_metadata(query):
    return list(container.query_items(
        query=query,
        enable_cross_partition_query=True
    ))