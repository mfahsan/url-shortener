FROM python:3.7.1
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt