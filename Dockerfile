FROM python:3.10
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Install package in development mode
RUN pip install -e .

# Set Python path and expose port
ENV PYTHONPATH=/app:$PYTHONPATH
EXPOSE 8000

# Development mode uses reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
