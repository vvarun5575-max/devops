FROM python:3.11-slim

WORKDIR /app

RUN app-get update && apt-get install -y ncbi-blast+

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ /app/

RUN mkdir /data 

COPY data/ /data /

EXPOSE 5000

 CMD ["python","app.py"]