FROM python:3.10

WORKDIR /app

COPY . .

ENV GOOGLE_APPLICATION_CREDENTIALS=./credentials.json

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "async_main.py"]
