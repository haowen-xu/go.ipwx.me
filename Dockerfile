FROM python:3.7-stretch

COPY . /app

RUN apt-get update && \
    apt-get -y dist-upgrade && \
    apt-get install pandoc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["bash", "/app/start.sh"]
