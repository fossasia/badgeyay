# Docker

![image](https://user-images.githubusercontent.com/35162705/45485499-7e21c880-b775-11e8-95d6-f377567f8f4e.png)

### Prerequisites

Before you begin this, ensure the following is installed to your system:

- Python 2.7 or 3.x,
- Docker, and
- A git repository to store your project and track changes.

## Create Dockerfile

Create a file named "Docker" with this content :

````
FROM ubuntu:16.04

MAINTAINER <your_name> "<your_mail> "

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    pip install --upgrade pip

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "application.py" ]
````

## Build Docker image

### Build with PATH :

Make sure you run this command from the same directory as the location of your Dockerfile
``$ docker build .``

Now run this command to see the Docker images you have in your local repository.
``docker images``

## Debug your build

If something goes wrong with the build you can fire up a plain ubuntu image and try installing each package from the Dockerfile manually.

Run this :
````
docker pull ubuntu:16.04
docker run -it -v [full file path to your app files]:/app ubuntu:16.04 /bin/bash
````
## Fire up your Docker container
Run this:
``docker run -p 5000:5000 -v [file path to the project files on your computer]:/app fossasia/badgeyay``

## Deploy on AWS Elastic Beanstalk

![image-1](https://user-images.githubusercontent.com/35162705/45485469-677b7180-b775-11e8-875a-df476bf939a2.png)

- Login to AWS and get to the Elastic Beanstalk service.
- Create a new environment and select “Docker” as the preconfigured platform.
- Upload a zip of your app files, which of course should include the Dockerfile. Create the zip from within the root directory of your app.

Once you have successfully uploaded your files on the right size instance, Elastic Beanstalk will deploy your app and make it available.

Cheers:

## demo deployment :

![screenshot - 9_13_2018 5_54_03 pm](https://user-images.githubusercontent.com/35162705/45485578-c345fa80-b775-11e8-9335-e1f72773cc80.png)

## Useful Links:

[Document](https://docs.docker.com)
