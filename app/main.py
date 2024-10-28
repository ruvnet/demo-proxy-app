from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.core.config import Settings
from app.api.v1.endpoints import (
    auth,
    chat,
    drive,
    events,
    feedback,
    integration,
    membership,
    projects,
    reports,
    sources,
    stories,
    storyplan,
    tako,
    twitter,
    users
)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load settings
settings = Settings()

app = FastAPI(
    title="Capitol AI Services API",
    description="Middleware API for Capitol AI Services",
    version="1.0.0",
    openapi_url="/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(chat.router, prefix="/api/v1", tags=["chat"])
app.include_router(drive.router, prefix="/api/v1", tags=["drive"])
app.include_router(events.router, prefix="/api/v1", tags=["events"])
app.include_router(feedback.router, prefix="/api/v1", tags=["feedback"])
app.include_router(integration.router, prefix="/api/v1", tags=["integration"])
app.include_router(membership.router, prefix="/api/v1", tags=["membership"])
app.include_router(projects.router, prefix="/api/v1", tags=["projects"])
app.include_router(reports.router, prefix="/api/v1", tags=["reports"])
app.include_router(sources.router, prefix="/api/v1", tags=["sources"])
app.include_router(stories.router, prefix="/api/v1", tags=["stories"])
app.include_router(storyplan.router, prefix="/api/v1", tags=["storyplan"])
app.include_router(tako.router, prefix="/api/v1", tags=["tako"])
app.include_router(twitter.router, prefix="/api/v1", tags=["twitter"])
app.include_router(users.router, prefix="/api/v1", tags=["users"])


# Define the request model for the specific POST request
class StoryPayload(BaseModel):
    story_id: str
    user_config_params: dict
    story_plan_config_id: str


# Helper function to add required headers
def add_custom_headers():
    return {
        "X-Domain": X_DOMAIN,
        "X-API-Key": X_API_KEY,
        "X-User-ID": USER_ID,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }


# POST endpoint for forwarding the specific payload
@app.post("/forward-story")
async def forward_story(payload: StoryPayload):
    headers = add_custom_headers()  # Add custom headers

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=FORWARD_URL,
            json=payload.dict(),  # Forward the request payload as JSON
            headers=headers,  # Include the custom headers
        )
        return Response(
            content=response.text,
            status_code=response.status_code,
            headers=dict(response.headers),
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
    custom_headers = add_custom_headers()
    logging.info(f"****")
    logging.info(f"Headers: {dict(custom_headers)}")

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=f"{forward_url}?{query_params}",
            headers=custom_headers,  # Add custom headers here
            content=body,
        )

    # Log the response for debugging
    logging.info(f"Forwarded response status: {response.status_code}")
    logging.info(f"Response content: {response.text}")

    # Return the response from the forwarded request, preserving the status code and headers
    # Return the response with JSON content and status code
    try:
        json_content = response.json()
        return Response(
            content=json.dumps(json_content),
            status_code=response.status_code,
            headers={"Content-Type": "application/json"},
        )
    except ValueError:
        # If the response is not JSON, fallback to returning it as text
        logging.error("Response content is not valid JSON")
        return Response(
            content=response.text,
            status_code=response.status_code,
            headers={
                "Content-Type": response.headers.get("Content-Type", "text/plain")
            },
        )

# Add this block to run the app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
