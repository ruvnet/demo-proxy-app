FROM python:3.10
WORKDIR /app
COPY . .

ENV PYTHONPATH=/app:$PYTHONPATH

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
