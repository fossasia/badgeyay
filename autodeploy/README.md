# Auto deployment

This directory contains a Python auto deployment script that polls the github
projects of Badgeyay and updates docker-compose containers

## Config format

Edit `config.yml` for adding new projects

Example config:
```yml
server:
    url: https://github.com/fossasia/badgeyay/api
    branch: development
    container: web
frontend:
    url: https://github.com/fossasia/badgeyay/frontend
    branch: development
```

As you can see, the `yaml` file contains the project name, github url, branch and upgrade commands for migrations or database creation. Every projects needs a `docker-compose.yml` file in the root directory for this to work.

## Running the process

After `docker` and `docker-compose` are installed on your system, execute

```bash
$ python3 autodeploy/main.py --workdir WORKDIR --config CONFIG
```
where, the WORKDIR and CONFIG are the location of your project and the config.yml file respectively.

Check out the log output for results.
