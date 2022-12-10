FROM python:3.10-alpine
ENV FLASK_APP=/app/main.py \
    FLASK_DEBUG=False \
    DATA_PATH="./data.json"
COPY requirements.txt requirements.txt
RUN pip install -r /requirements.txt
COPY app /app
WORKDIR app
CMD ["gunicorn", "--conf", "gunicorn_conf.py", "--bind", "0.0.0.0:80", "main:app"]
