FROM python:3-slim
LABEL maintainer="Yash Ladha <yashladhapankajladha123@gmail.com>"


ENV INSTALL_PATH /badgeyay
RUN mkdir -p "$INSTALL_PATH"

WORKDIR $INSTALL_PATH

# apt-get update and update some packages
RUN apt-get update && apt-get install --no-install-recommends -y wget git ca-certificates curl && update-ca-certificates && apt-get clean -y


# install deps
RUN apt-get install -y --no-install-recommends build-essential python3-dev libpq-dev libevent-dev libmagic-dev && apt-get clean -y
RUN apt-get install -y --no-install-recommends libpango1.0-0 libcairo2 libpq-dev python3-pip && apt-get clean -y

# copy just requirements
COPY requirements.txt requirements.txt

# install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# copy remaining files
COPY . .

CMD ["gunicorn", "-b", ":8080", "api.run:app"]
