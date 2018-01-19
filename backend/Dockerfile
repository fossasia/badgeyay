FROM python:3.6

# We copy just the requirements.txt first to leverage Docker cache
COPY ./app/requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]

