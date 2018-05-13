# Configuration variable for the application
from . import config

if config.DEBUG:
    BASE_URL = 'http://localhost:5000/'
    BASE_FRONTEND_URL = 'http://localhost:4200/'
else:
    BASE_URL = 'http://badgeyay-api.herokuapp.com/'
    BASE_FRONTEND_URL = 'http://badgeyay.com/'
