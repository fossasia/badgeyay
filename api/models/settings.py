from api.db import db


class ApplicationEnvironament:

    def __init__(self):
        pass
    DEVELOPMENT = 'development'
    STAGING = 'staging'
    PRODUCTION = 'production'
    TESTING = 'testing'


class Settings(db.Model):
    __tablename__ = 'settings'

    app_environment = db.Column(db.String, default=ApplicationEnvironament.PRODUCTION)
    # Name of the application. (Eg. Badgeyay)
    app_name = db.Column(db.String)
    # Description of the App
    app_description = db.Column(db.String(140))
    # App secret
    secret = db.Column(db.String)

    # -------------
    # Storage
    # -------------

    # storage place local, s3,etc
    storage_place = db.Column(db.String)
    # S3
    aws_key = db.Column(db.String)
    aws_secret = db.Column(db.String)
    aws_bucket_name = db.Column(db.String)
    aws_region = db.Column(db.String)
    # Google Storage
    gs_key = db.Column(db.String)
    gs_secret = db.Column(db.String)
    gs_bucket_name = db.Column(db.String)
    # Azure Storage
    azure_account_name = db.Column(db.String)
    azure_account_key = db.Column(db.String)
    azure_container_name = db.Column(db.String)

    # -------------
    # Social Login
    # -------------

    # Google Auth is handled by Firebase
    # FB auth
    fb_client_id = db.Column(db.String)
    fb_client_secret = db.Column(db.String)
    # Twitter auth
    tw_consumer_key = db.Column(db.String)
    tw_consumer_secret = db.Column(db.String)

    # -------------
    # Payment Gateway
    # -------------

    # Stripe Keys
    stripe_client_id = db.Column(db.String)
    stripe_secret_key = db.Column(db.String)
    stripe_publishable_key = db.Column(db.String)
    # PayPal Credentials
    paypal_mode = db.Column(db.String)
    paypal_sandbox_username = db.Column(db.String)
    paypal_sandbox_password = db.Column(db.String)
    paypal_sandbox_signature = db.Column(db.String)
    paypal_live_username = db.Column(db.String)
    paypal_live_password = db.Column(db.String)
    paypal_live_signature = db.Column(db.String)

    # -------------
    # EMAIL
    # -------------

    # Email service. (sendgrid,smtp)
    email_service = db.Column(db.String)
    email_from = db.Column(db.String)
    email_from_name = db.Column(db.String)
    # Sendgrid
    sendgrid_key = db.Column(db.String)
    # SMTP
    smtp_host = db.Column(db.String)
    smtp_username = db.Column(db.String)
    smtp_password = db.Column(db.String)
    smtp_port = db.Column(db.Integer)
    smtp_encryption = db.Column(db.String)
    # Mail Server
    mail_server = db.Column(db.String)
    mail_port = db.Column(db.Integer)
    mail_use_tls = db.Column(db.String)
    mail_use_ssl = db.Column(db.String)
    mail_username = db.Column(db.String)
    mail_password = db.Column(db.String)
    mail_default_server = db.Column(db.String)

    # -------------
    # ANALYTICS
    # -------------

    # Google Analytics
    analytics_key = db.Column(db.String)

    # -------------
    # Social links
    # -------------

    support_url = db.Column(db.String)
    google_url = db.Column(db.String)
    github_url = db.Column(db.String)
    twitter_url = db.Column(db.String)
    facebook_url = db.Column(db.String)
    youtube_url = db.Column(db.String)

    def __init__(self,
                 app_environment=ApplicationEnvironament.PRODUCTION,
                 app_name=None,
                 app_description=None,
                 secret=None,
                 storage_place=None,
                 aws_key=None,
                 aws_secret=None,
                 aws_bucket_name=None,
                 aws_region=None,
                 gs_key=None,
                 gs_secret=None,
                 gs_bucket_name=None,
                 azure_account_name=None,
                 azure_account_key=None,
                 azure_container_name=None,
                 fb_client_id=None,
                 fb_client_secret=None,
                 tw_consumer_key=None,
                 tw_consumer_secret=None,
                 stripe_client_id=None,
                 stripe_secret_key=None,
                 stripe_publishable_key=None,
                 paypal_mode=None,
                 paypal_sandbox_username=None,
                 paypal_sandbox_password=None,
                 paypal_sandbox_signature=None,
                 paypal_live_username=None,
                 paypal_live_password=None,
                 paypal_live_signature=None,
                 email_service=None,
                 email_from=None,
                 email_from_name=None,
                 sendgrid_key=None,
                 smtp_host=None,
                 smtp_username=None,
                 smtp_password=None,
                 smtp_port=None,
                 smtp_encryption=None,
                 mail_server=None,
                 mail_port=None,
                 mail_use_tls=None,
                 mail_use_ssl=None,
                 mail_username=None,
                 mail_password=None,
                 mail_default_server=None,
                 analytics_key=None,
                 support_url=None,
                 google_url=None,
                 github_url=None,
                 twitter_url=None,
                 facebook_url=None,
                 youtube_url=None):

        self.app_environment = app_environment
        self.app_name = app_name
        self.app_description = app_description
        self.secret = secret
        self.storage_place = storage_place
        self.aws_key = aws_key
        self.aws_secret = aws_secret
        self.aws_bucket_name = aws_bucket_name
        self.aws_region = aws_region
        self.gs_key = gs_key
        self.gs_secret = gs_secret
        self.gs_bucket_name = gs_bucket_name
        self.azure_account_name = azure_account_name
        self.azure_account_key = azure_account_key
        self.azure_container_name = azure_container_name
        self.fb_client_id = fb_client_id
        self.fb_client_secret = fb_client_secret
        self.tw_consumer_key = tw_consumer_key
        self.tw_consumer_secret = tw_consumer_secret
        self.stripe_client_id = stripe_client_id
        self.stripe_secret_key = stripe_secret_key
        self.stripe_publishable_key = stripe_publishable_key
        self.paypal_mode = paypal_mode
        self.paypal_sandbox_username = paypal_sandbox_username
        self.paypal_sandbox_password = paypal_sandbox_password
        self.paypal_sandbox_signature = paypal_sandbox_signature
        self.paypal_live_username = paypal_live_username
        self.paypal_live_password = paypal_live_password
        self.paypal_live_signature = paypal_live_signature
        self.email_service = email_service
        self.email_from = email_from
        self.email_from_name = email_from_name
        self.sendgrid_key = sendgrid_key
        self.smtp_host = smtp_host
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.smtp_port = smtp_port
        self.smtp_encryption = smtp_encryption
        self.mail_server = mail_server
        self.mail_port = mail_port
        self.mail_use_tls = mail_use_tls
        self.mail_use_ssl = mail_use_ssl
        self.mail_username = mail_username
        self.mail_password = mail_password
        self.mail_default_server = mail_default_server
        self.analytics_key = analytics_key
        self.support_url = support_url
        self.google_url = google_url
        self.github_url = github_url
        self.twitter_url = twitter_url
        self.facebook_url = facebook_url
        self.youtube_url = youtube_url

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

    def __repr__(self):
        return 'Settings'

    def __str__(self):
        return self.__repr__()
