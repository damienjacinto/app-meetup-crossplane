FROM python:3.10-alpine
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
COPY requirements.txt requirements.txt
RUN pip install -r /requirements.txt
COPY app /app
WORKDIR /app
RUN ls