import numpy as np

def process_video(video_url):
    # Example implementation for processing the video
    # Replace with actual video processing logic
    vectors = np.random.rand(10, 128).tolist()
    metadata = {
        "id": "unique_video_id",
        "video_url": video_url,
        "tags": ["example", "tags"],
        "description": "Sample video description",
        "transcripts": "Sample transcribed text",
        "timestamps": [0, 120, 240],
        "vectors": vectors
    }
    return metadata
