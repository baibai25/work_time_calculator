FROM python:3.9

RUN apt-get update -y && apt-get upgrade -y

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt
