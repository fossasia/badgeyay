# Heroku

you may use a production-ready web server such as Gunicorn.

``$ pip install gunicorn``

Now, run your app with:

``$ gunicorn manage:app``

Gunicorn uses port 8000 instead of 5000.

### Heroku Setting Up

Create an account at Heroku.com

Install Git and Heroku Toolbelt

You can find instructions at Heroku.com.

For example, if you are in an AWS EC2 Ubuntu instance, you can use:

````
$ sudo apt-get install -y git-core
$ wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
````

You can check if it worked with:

````
$ which git
$ which heroku
````

Now, login at Heroku:

``$ heroku login``

Authorize your Machine at Heroku

Create and add a SSH Key at Heroku:

````
$ ssh-keygen -t rsa
$ heroku keys:add
````

The public and private keys will be at ~/.ssh.

### Creating a Git Repository

Heroku's push/commits work just like as Git. But instead of using the "origin" you use "heroku".

``$ git push origin master``

and the deployment at Heroku (production) is done using:

``$ git push heroku master``

In the root of your project, go ahead and create a Git repository, commit, add, push:

````
$ git init
$ git add -A
$ git commit -m "First commit"
$ git push origin master
````

### The Heroku Repository

Now, let's create our app at Heroku:

``$ heroku create <app-name>``

Addons and Environment Variables:

Now it's time to add the addons and the environment variables to your app at the Heroku server. For the app I mentioned in the beginning, I type:

````
$ heroku addons:add heroku-postgresql:dev
$ heroku pg:promote HEROKU_POSTGRESQL_ONYX_URL
$ heroku config:set MAIL_USERNAME="<login>"
$ heroku config:set MAIL_PASSWORD="<password>"
````

Adding Requirements :

Heroku needs to know what libraries and packages it needs to install to be able to run your application. For this, create a file requirements.txt in the root of your app, with all the libraries from your environment.

``$ cat pip freeze >> requirements.txt``

### Creation of Procfile :

Create a file named Procfile. The content should be :

``web gunicorn manage:app``

### Using Foreman to Emulate Heroku

The Heroku Toolbet includes Foreman, used to run the app locally through the Procfile for testing purposes. The environment variables set at Heroku must be defined locally. Just create a file var.env with this information:

````
FLASK_CONFIG=heroku
MAIL_USERNAME=<your-username>
MAIL_PASSWORD=<your-password>
````

Foreman run is used to run commands under the environment of the application. Foreman start reads the Procfile and executes the tasks in it:

````
$ foreman run python manage.py deploy
$ foreman start
````

### Configuring Logging

````
class HerokuConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

    import logging
    from logging import StreamHandler
    file_handler = StreamHandler()
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
````
To let Heroku know what configuration it should use, add this environment variavle :

``$ heroku config:set FLASK_CONFIG=heroku``

## Deploying!

If everything is good, it's time to deploy your application.

Run this command :

``$ git push heroku master``

That's it! The app should be running at < app-name >.hero‐
kuapp.com. 
Cheers.
