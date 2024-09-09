import os
import logging
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
import httpx

app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO)

# Get the API URL from the environment variable
FORWARD_URL = os.getenv("API_URL", "https://example.com")  # Replace with your default or environment variable

# Define the request model for the specific POST request
class StoryPayload(BaseModel):
    story_id: str
    user_config_params: dict
    story_plan_config_id: str

# POST endpoint for forwarding the specific payload
@app.post("/forward-story")
async def forward_story(payload: StoryPayload):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=FORWARD_URL,
            json=payload.dict()  # Forward the request payload as JSON
        )
        return Response(
            content=response.text,
            status_code=response.status_code,
            headers=dict(response.headers)
        )

# Catch-all route that forwards any request (with method, params, and body)
@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def catch_all(request: Request, path: str):
    # Construct the full URL to forward the request
    forward_url = f"{FORWARD_URL}/{path}"

    # Extract query params
    query_params = request.url.query

    # Log the incoming request details for debugging
    logging.info(f"Incoming request: {request.method} {request.url}")
    logging.info(f"Headers: {dict(request.headers)}")
    logging.info(f"Query params: {query_params}")
    try:
        body = await request.body()
        logging.info(f"Body: {body.decode('utf-8')}")
    except Exception as e:
        logging.error(f"Error reading body: {e}")

    # Prepare the forwarding request
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=f"{forward_url}?{query_params}",
            headers=request.headers.raw,
            content=await request.body()
        )

    # Log the response for debugging
    logging.info(f"Forwarded response status: {response.status_code}")
    logging.info(f"Response content: {response.text}")

    # Return the response from the forwarded request, preserving the status code and headers
    return Response(
        content=response.text,
        status_code=response.status_code,
        headers=dict(response.headers)
    )
