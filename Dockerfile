FROM python:3.10
WORKDIR /app

# Install pip-tools
RUN pip install pip-tools

# Copy requirements files
COPY requirements.in .
COPY setup.py .

# Generate and install requirements
RUN pip-compile requirements.in
RUN pip-sync requirements.txt

# Copy the rest of the code
COPY . .

# Install package in development mode
RUN pip install -e .

# Set Python path and expose port
ENV PYTHONPATH=/app:$PYTHONPATH
EXPOSE 8000

# Development mode uses reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
