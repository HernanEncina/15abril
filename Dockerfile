FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install flask

WORKDIR /app
COPY . .

CMD ["python3", "procesador.py", "data.csv"]