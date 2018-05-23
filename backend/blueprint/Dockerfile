FROM ubuntu:16.04

LABEL Name=badgeyay
LABEL MAINTAINER="hi@vaibhavsingh97.com"

RUN apt-get update && apt-get install --no-install-recommends \
    -y build-essential python python-dev python3.5 python3.5-dev \
    python-pip virtualenv libssl-dev libpq-dev \
    git build-essential libfontconfig1 libfontconfig1-dev \ 
    libpango1.0-0 libcairo2 libpq-dev python-cairosvg \
    && rm -rf /var/lib/apt/lists/*
RUN pip install setuptools pip --upgrade --force-reinstall
RUN pip install HTML

WORKDIR /app
COPY . /app

RUN virtualenv -p /usr/bin/python3.5 /venv/
RUN /bin/bash -c "source /venv/bin/activate"

RUN pip install -r api/requirements.txt

CMD ["gunicorn", "-b", ":8080", "api.run:app"]
