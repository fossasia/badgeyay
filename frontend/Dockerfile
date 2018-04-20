FROM node:8.9.4

WORKDIR /usr/src/app

COPY package*.json ./

RUN docker -d &
RUN npm config set strict-ssl false
RUN apt-get update
RUN apt-get install -y nodejs
RUN npm cache verify
RUN npm install -g -D ember-cli 
RUN npm config set registry=https://registry.npmjs.com/
RUN npm install -D

COPY . .

EXPOSE 4200

CMD ["ember", "serve"]
