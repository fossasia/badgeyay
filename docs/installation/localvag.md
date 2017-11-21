# Local Development Setup

The instructions on this page will guide you in setting up a local development
environment in your system. First things first, BadgeYay needs `Python 3` to run.

### Vagrant Installation Instructions
1. Install Vagrant from [Vagrant Download Page](https://www.vagrantup.com/downloads.html)
2. Install Virtualbox from [Vitualbox Download Page](https://www.virtualbox.org/wiki/Downloads)
3. Clone the project from `git clone https://github.com/<your_username>/badgeyay.git`
4. Enter the directory using `cd badgeyay`
5. In Terminal in the "badgeyay" directory, type `vagrant up` to bring up the virtual machine. This will start installation of a ubuntu box within which the server will run with all its components. If after typing "vagrant up" you received an error stating “valid providers not found ...", type `vagrant up --provider=virtualbox`
6. After the installation is completed `ssh` into vagrant environment using `vagrant ssh`. This will bring you to the root directory of the Virtual Machine
7. Move to your project using `cd /vagrant`
8. To Run the flask server you need to be in the "app" directory. Do `cd app`
9. Run flask server in port `0.0.0.0`
   ```
   export FLASK_APP=main.py
   python -m flask run --host=0.0.0.0
   ```
10. Now your server is up and running. To view the badgeyay page go to localhost:8001
