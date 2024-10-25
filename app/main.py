import os
import logging
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
import httpx

app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO)

# Get the API URL and other variables from environment variables
FORWARD_URL = os.getenv("API_URL", "https://example.com")  # Replace with your default or environment variable
X_DOMAIN = os.getenv("DOMAIN", "your-default-domain")  # Replace with your domain or environment variable
X_API_KEY = os.getenv("API_KEY", "your-default-api-key")  # Replace with your API key or environment variable
USER_ID = "1"  # Hardcoded user ID

# Define the request model for the specific POST request
class StoryPayload(BaseModel):
    story_id: str
    user_config_params: dict
    story_plan_config_id: str

# Helper function to add required headers
def add_custom_headers(headers):
    headers.update({
        "X-Domain": X_DOMAIN,
        "X-API-Key": X_API_KEY,
        "X-User-ID": "1"
    })

    print("printed X_DOMAIN", X_DOMAIN)
    print("printed X_API_KEY", X_API_KEY)
    print("printed FORWARD_URL", FORWARD_URL)
    print("printed headers", headers)
    return headers

# POST endpoint for forwarding the specific payload
@app.post("/forward-story")
async def forward_story(payload: StoryPayload):
    headers = add_custom_headers({})  # Add custom headers
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=FORWARD_URL,
            json=payload.dict(),  # Forward the request payload as JSON
            headers=headers  # Include the custom headers
        )
        return Response(
            content=response.text,
            status_code=response.status_code,
            headers=dict(response.headers)
        )

# Catch-all route that forwards any request (with method, params, and body)
@app.api_route("/api/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])

async def catch_all(request: Request, path: str):
    # Construct the full URL to forward the request
    forward_url = f"{FORWARD_URL}/api/{path}"

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
    custom_headers = add_custom_headers(dict(request.headers))
    logging.info(f"****")
    logging.info(f"Headers: {dict(custom_headers)}")

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=f"{forward_url}?{query_params}",
            headers=custom_headers,  # Add custom headers here
            content=body
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
