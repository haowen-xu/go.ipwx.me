FROM python:3.7-stretch

COPY . /app

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install -y pandoc && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["bash", "/app/start.sh"]
