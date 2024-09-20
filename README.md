
# DEMO PROXY API Proxy

This is a FastAPI application that acts as a proxy for forwarding requests to the Capitol API. It adds custom headers to the requests and logs the incoming and outgoing requests for debugging purposes.

## Introduction

The primary purpose of this application is to forward requests to a specified API URL while adding custom headers. It provides two main functionalities:

1. A dedicated endpoint `/forward-story` for forwarding a specific payload with custom headers.
2. A catch-all route `/api/{path:path}` that forwards any request (GET, POST, PUT, DELETE, PATCH) to the specified API URL, adding custom headers.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Faction-V/demo-proxy-app
cd demo-proxy-app
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set the following environment variables:

- `API_URL`: The URL of the API to forward requests to (e.g., `https://example.com`).
- `DOMAIN`: The domain value to be included in the `X-Domain` header.
- `API_KEY`: The API key value to be included in the `X-API-Key` header.

## Usage

1. Start the FastAPI application:

```bash
uvicorn main:app --reload
```

2. Send requests to the appropriate endpoints:

- For the `/forward-story` endpoint, send a POST request with a JSON payload containing `story_id`, `user_config_params`, and `story_plan_config_id` fields.
- For other requests, use the `/api/{path:path}` endpoint, where `{path:path}` represents the path of the API you want to forward the request to.

The application will log the incoming request details, forward the request to the specified `API_URL` with the added custom headers, and return the response from the API.

## Contributing

Contributions are welcome! Please follow the standard GitHub workflow:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Open a pull request

## License

This project is licensed under the [MIT License](LICENSE).

