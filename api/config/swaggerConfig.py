class SwaggerConfig(object):
    SWAGGER = {
        "swagger": "3.0",
        "title": "Badgeyay Documentation",
        "description": "An API which genrates printable badges in a PDF",
        'uiversion': 3,
        "headers": [
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
            ('Access-Control-Allow-Credentials', "true"),
        ],
        "version": "1.0.1",
        "contact": {
            "responsibleOrganization": "FOSSASIA",
            "responsibleDeveloper": "FOSSASIA",
            "email": "fossasia@googlegroups.com",
            "url": "https://fossasia.org/",
        },
        "schemes": [
            "http",
            "https"
        ],
        "consumes": [
            "application/json",
        ],
        "produces": [
            "application/json",
        ],
    }