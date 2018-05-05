# Configuration variable for the application
from . import config

if config.DEBUG:
    BASE_URL = 'http://localhost:5000/'
else:
    BASE_URL = 'http://badgeyay-api.herokuapp.com/'
