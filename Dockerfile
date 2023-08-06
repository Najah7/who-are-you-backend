FROM python:3.9.17-bullseye

LABEL container="Najah7"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY . /app

WORKDIR /app

EXPOSE 8000

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && apt-get remove -y gcc \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]