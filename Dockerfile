FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py ./

ENV ACCESS_TOKEN=$ACCESS_TOKEN
ENV REPO_NAME=$REPO_NAME
ENV README_FILE_NAME=$README_FILE_NAME

RUN apt-get update && apt-get -y install cron

COPY cronjob.txt ./
RUN crontab cronjob.txt

CMD ["cron", "-f"]
