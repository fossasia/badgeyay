# Flask-Vagrant-Setup

- Configure a Flask app on a VM using Vagrant, with provisioning handled by Ansible i.e setting up python, virtualenv, nginx, gunicorn, etc.

### Prerequisite

You need to install:

- Git
- [Vagrant](Vagranthttps://www.vagrantup.com/downloads.html)
- I will be using VirtualBox for this setup, you can grab a copy for your OS [here](https://www.virtualbox.org/wiki/Downloads).
- If you use VirtualBox download it [here](https://www.virtualbox.org/wiki/Downloads).

### Creation of Vagrant file :

Type the following commands in a new file and save it as ``Vagrantfile`` :
````
# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
VAGRANT_IP = "10.0.0.5"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network :private_network, ip: VAGRANT_IP

  # -- if you don't fancy private ip, you can use the below --
  # -- note however that by doing so, the 'provision' IP will need to change --
  
  # port forwarding to allow access to the app running on the guest OS
  # from a dedicated port on the host machine
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # run Ansible from the Vagrant VM
  config.vm.provision "ansible_local" do |ansible|
    ansible.install = true
    ansible.playbook = ".provisioning/deploy.yml"
  end

  # add localhost to Ansible inventory
  config.vm.provision "shell", inline: "printf 'localhost\n' | sudo tee /etc/ansible/hosts > /dev/null"

  # increase VM RAM size
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end
end
````

### clone this repo and cd into it:
````
git clone https://github.com/fossasia/badgeyay.git .
cd badgeyay
````
### Boot up your Vagrant environment:

``vagrant up``

_This may take less or more than a minute depending on your internet connection (so be patient)._

- Vagrant runs the virtual machine without a UI. To prove that it is running, you can SSH into the machine:

```
vagrant ssh
```
### Access app

Point your browser to: [http://10.0.0.5](http://10.0.0.5)

Cheers :beers:

