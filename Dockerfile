FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py ./

ENV ACCESS_TOKEN=$ACCESS_TOKEN
ENV REPO_NAME=$REPO_NAME
ENV FILE_NAME=$FILE_NAME
ENV SCHEDULE="07:00"
ENV TZ=Asia/Tehran

CMD python3 app.py
