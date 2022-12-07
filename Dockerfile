FROM python:3.10-alpine
ENV FLASK_APP=/app/main.py
ENV FLASK_ENV=production
COPY requirements.txt requirements.txt
RUN pip install -r /requirements.txt
COPY app /app
WORKDIR /app
CMD flask run