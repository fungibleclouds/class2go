import os

if os.environ.has_key('C2G_JENKINS_DBNAME'):
  DBNAME = os.environ.get('C2G_JENKINS_DBNAME')
else:
  DBNAME = 'class2go'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DBNAME,                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = ''

# When PRODUCTION=True we don't show stackdumps on errors
PRODUCTION = False
INSTANCE = "jenkins"

# Put your name and email address here, so Django serious errors can come to you
ADMINS = (
        ('Class2Go Jenkins', 'c2g-dev@cs.stanford.edu')
        )

# Secrets used for S3 - Sef
AWS_ACCESS_KEY_ID = 'local'
AWS_SECRET_ACCESS_KEY = 'local'
AWS_STORAGE_BUCKET_NAME = 'local'

# MEDIA_ROOT = '/opt/class2go/uploads'

PIAZZA_ENDPOINT = "https://piazza.com/basic_lti"
PIAZZA_KEY = "class2go.testing"
PIAZZA_SECRET = "piazza_secret_test"

# SMTP INFO for SES -- Amazon Simple Email Service $1 per 10K recipients
SES_SMTP_USER = ''
SES_SMTP_PASSWD = ''

# old credentials

# new credentials
YT_SERVICE_DEVELOPER_KEY = ''
GOOGLE_CLIENT_ID = ''
GOOGLE_CLIENT_SECRET = ''

