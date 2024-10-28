FROM python:3.10
WORKDIR /app
COPY . .

# Set Python path to include the app directory 
ENV PYTHONPATH=/app:$PYTHONPATH

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000
