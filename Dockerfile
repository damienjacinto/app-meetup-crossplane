FROM python:3.10-alpine
ENV FLASK_APP=/app/main.py
ENV FLASK_DEBUG=False
COPY requirements.txt requirements.txt
RUN pip install -r /requirements.txt
COPY app /app
CMD ["gunicorn", "--conf", "/app/gunicorn_conf.py", "--bind", "0.0.0.0:80", "app.main:app"]