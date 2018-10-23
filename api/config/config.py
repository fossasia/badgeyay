from envparse import env

# DEBUG variable
DEBUG = env.bool('BADGEYAY_DEBUG', default=True)

# Environment for working, can be LOCAL/PROD
ENV = env.str('BADGEYAY_ENV', default='PROD')

# Sample config for PostgreSQL Database
POSTGRES = {
    'user': env.str('BADGEYAY_DATABASE_OWNER', default='postgres'),
    'pw': env.str('BADGEYAY_DATABASE_PASSWORD', default='postgres'),
    'host': 'localhost',
    'port': '5432',
    'db': env.str('BADGEYAY_DATABASE', default='badgeyay'),
    'secret': 'thisisaverysupersecretkeyforfossasiabadgeyay'
}

# Posts per page to be shown
POSTS_PER_PAGE = 10

admins = ['badgeyayofficial@gmail.com']
