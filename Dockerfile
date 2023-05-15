FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py ./

ENV ACCESS_TOKEN=<access_token_value>
ENV REPO_NAME=<repo_name_value>
ENV README_FILE_NAME=<readme_file_name_value>

RUN apt-get update && apt-get -y install cron

COPY cronjob.txt ./
RUN crontab cronjob.txt

CMD ["cron", "-f"]
