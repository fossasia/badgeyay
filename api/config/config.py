from envparse import env

# DEBUG variable
DEBUG = env.bool('BADGEYAY_DEBUG', default=True)

# Environment for working, can be LOCAL/PROD
ENV = env.str('BADGEYAY_ENV', default='PROD')

# Sample config for PostgreSQL Database
POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'db': 'badgeyay',
    'secret': 'thisisaverysupersecretkeyforfossasiabadgeyay'
}

# Posts per page to be shown
POSTS_PER_PAGE = 10

admins = ['badgeyayofficial@gmail.com']
