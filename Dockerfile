FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app

COPY procesador.py .
COPY data.csv .

CMD ["python3", "procesador.py", "data.csv"]