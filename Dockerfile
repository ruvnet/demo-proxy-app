FROM python:3.10
WORKDIR /app

# Install pip-tools
RUN pip install pip-tools

# Copy requirements files
COPY requirements.txt .

# Install requirements
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Set Python path and expose port
ENV PYTHONPATH=/app
EXPOSE 8000

# Development mode uses reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
