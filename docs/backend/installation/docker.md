# Docker

[![Deploy to Docker ](https://files.cloud.docker.com/images/deploy-to-dockercloud.svg)](https://cloud.docker.com/stack/deploy/?repo=https://github.com/fossasia/badgeyay)

* Get the latest version of docker. See the [offical site](https://docs.docker.com/engine/installation/) for installation info for your platform.

* Install the latest version of docker-compose. Windows and Mac users should have docker-compose by default as it is part of Docker toolbox. For Linux users, see the
[official guide](https://docs.docker.com/compose/install/).

* Run `docker` and `docker-compose` in terminal to see if they are properly installed.

## Steps to deploy the backend to Docker

* **Step 1** - Clone the project and `cd` into it.

```bash
git clone https://github.com/fossasia/badgeyay.git && cd badgeyay/backend
```

* **Step 2** - Then set the required `SERVER_NAME` environment variable. `SERVER_NAME` should the same as the domain on which the server is running and it should not include 'http', 'https',
'www' or the trailing slash (/) in the url. Examples - `domain.com`, `sub.domain.com`, `sub.domain.com:5000` etc

```bash
export SERVER_NAME=localhost;
```

* **Step 3** - In the same terminal windows, run `docker-compose build` to build badgeyay's docker image. This process can take some time.

* **Step 4** - After the build is done, run `docker-compose up` to start the server.

* *NOTE* - If you are doing this for the first time, you will have to create the database and then the tables. So, keeping `docker-compose up` active in one terminal window, open another open in the same directory. In there, type the following command

```bash
docker-compose run postgres psql -h postgres -p 5432 -U postgres --password
```

* Write `test` as password and press ENTER. When inside psql shell, write the following command -

```sql
create database badgeyay;
# CREATE DATABASE
```
* Then exit the shell by typing `\q` and press ENTER.

* **Step 5** - Go to 'localhost' on the web browser and Badgeyay will be live

### Updating the Docker image

To update the Docker image with a more recent version of open-event-server, follow the same steps.

* **Step 1** - In the same directory as mentioned above, write `docker-compose build` followed by `docker-compose up` in the terminal.

* **Step 2** - Then open a new terminal window in the same directory and run the following command.

```bash
docker-compose run web python3 manage.py db upgrade
```

* **Step 3** - Then open 'localhost' in web browser to view the updated version of Badgeyay.
