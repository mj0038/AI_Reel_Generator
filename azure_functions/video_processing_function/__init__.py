import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    video_url = req.params.get('video_url')
    if not video_url:
        return func.HttpResponse(
            "Please pass a video_url in the query string",
            status_code=400
        )

    # For now, just return the video_url to ensure it's received correctly
    return func.HttpResponse(f"Video URL received: {video_url}", status_code=200)
