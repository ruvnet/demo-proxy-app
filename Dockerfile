FROM python:3.10
WORKDIR /app
COPY . .

# Install the package in development mode
RUN pip install -e .

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set Python path to include the app directory 
ENV PYTHONPATH=/app:$PYTHONPATH

# Expose the port the app runs on
EXPOSE 8000
