import sys
import os
import requests
import gradio as gr

# Add the root of the project to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from video_upload.main import upload_video
from video_processing.model import process_video
from metadata_storage.cosmos_db import store_metadata

def process_input(video, prompt):
    # Save the video locally for testing
    video_path = os.path.join(os.getcwd(), video.name)
    with open(video_path, "wb") as f:
        f.write(video.read())

    # Upload the video
    video_url = upload_video(video_path)

    # Process the video
    metadata = process_video(video_url)

    # Store the metadata
    store_metadata(metadata)

    return "Video processed and metadata stored!"

iface = gr.Interface(
    fn=process_input,
    inputs=["file", "text"],
    outputs="text",
    title="Video Reel Generator",
    description="Upload your video or provide a YouTube link to generate short-form content."
)

if __name__ == "__main__":
    iface.launch()
