"""
Django settings for hgapp project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

try:
    os.environ['SECRET_KEY']
    DEBUG = False
except:
    DEBUG = True

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = PROJECT_ROOT

if DEBUG:
    ALLOWED_HOSTS = [
        '127.0.0.1',
        'localhost'
    ]
else:
    ALLOWED_HOSTS = [
        'hgapp-dev.us-west-2.elasticbeanstalk.com',
        'thecontractgame.com',
        'www.thecontractgame.com',
    ]
    SESSION_COOKIE_DOMAIN = ".thecontractgame.com"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

#TODO: figure out a place to deployably serve our static files from that doesn't serve source
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static", "dist"),
]

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# List of finder classes that know how to find static files in
# various locations.

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler"
]
if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media-root')
else:
    AWS_DEFAULT_ACL = None
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME']


# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG:
    SECRET_KEY = '(35@*@4v-wy68tnjx*8pfzk4al=5pwa(2yaur=eoeqa8f@mb#c'
else:
    SECRET_KEY = os.environ['SECRET_KEY']

# Application definition

INSTALLED_APPS = [
    'powers.apps.PowersConfig',
    'profiles.apps.ProfilesConfig',
    'characters.apps.CharactersConfig',
    'games.apps.GamesConfig',
    'overrides.apps.OverridesConfig',
    'cells.apps.CellsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # theme
    "bootstrapform",
    "pinax_theme_bootstrap",

    # external
    "account",
    "pinax.eventlog",
    "pinax.webanalytics",
    'guardian',
    'pagedown.apps.PagedownConfig',
    'markdown_deux',
    'postman',

    #Wiki
    #'django.contrib.sites.apps.SitesConfig',
    'django.contrib.humanize.apps.HumanizeConfig',
    'django_nyt.apps.DjangoNytConfig',
    'mptt',
    'sekizai',
    'sorl.thumbnail',
    'wiki.apps.WikiConfig',
    'wiki.plugins.attachments.apps.AttachmentsConfig',
    'wiki.plugins.notifications.apps.NotificationsConfig',
    'wiki.plugins.images.apps.ImagesConfig',
    'wiki.plugins.macros.apps.MacrosConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'hgapp.middleware.TimezoneMiddleware'
]

ROOT_URLCONF = 'hgapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [
            os.path.join(PACKAGE_ROOT, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            "debug": DEBUG,
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "account.context_processors.account",
                "pinax_theme_bootstrap.context_processors.theme",
                "postman.context_processors.inbox",
                "sekizai.context_processors.sekizai", # required by Wiki
            ],
        },
    },
]

WSGI_APPLICATION = 'hgapp.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'applogfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'APPNAME.log'),
            'maxBytes': 1024*1024*15, # 15MB
            'backupCount': 1,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'applogfile'],
        },
        'django.request': {
            'handlers': ['mail_admins', 'applogfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console', 'applogfile'],
        },
    }
}

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SITE_ID = int(os.environ.get("SITE_ID", 1))

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    DEFAULT_FROM_EMAIL = 'thecontractgame@gmail.com'
    SERVER_EMAIL = 'thecontractgame@gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'thecontractgame@gmail.com'
    EMAIL_HOST_PASSWORD = os.environ["EMAIL_PASS"]


ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_USE_AUTH_AUTHENTICATE = True

AUTHENTICATION_BACKENDS = [
    "account.auth_backends.UsernameAuthenticationBackend",
    'guardian.backends.ObjectPermissionBackend',
]

#Postman settings
POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_AUTO_MODERATE_AS = True

#Pagedown settings
PAGEDOWN_WIDGET_CSS = ("overrides/pagedown_widget.css",)

#Wiki settings
def is_admin(request=None, user=None):
    if user is None:
        return request.user.is_superuser
    else:
        return user.is_superuser

WIKI_ACCOUNT_HANDLING = False
WIKI_ACCOUNT_SIGNUP_ALLOWED = False
WIKI_ANONYMOUS_WRITE = False
WIKI_CAN_WRITE = is_admin
WIKI_CAN_MODERATE = is_admin
WIKI_CAN_DELETE = is_admin
WIKI_CAN_CHANGE_PERMISSIONS = is_admin
WIKI_CAN_ASSIGN_OWNER = is_admin
WIKI_CAN_ASSIGN = is_admin
WIKI_CAN_ADMIN = is_admin
WIKI_REVISIONS_PER_HOUR = 120
if not DEBUG:
    WIKI_USE_LOCAL_PATH = False

WIKI_MARKDOWN_HTML_ATTRIBUTES = {'a': ['aria-controls', 'aria-expanded', 'href', 'title', 'class', 'data-toggle', 'id', 'target', 'rel'],
                                 'abbr': ['title', 'class', 'id', 'target', 'rel'],
                                 'acronym': ['title', 'class', 'id', 'target', 'rel'],
                                 'b': ['class', 'id', 'target', 'rel'], 'blockquote': ['class', 'id', 'target', 'rel'],
                                 'br': ['class', 'id', 'target', 'rel'],
                                 'code': ['class', 'id', 'target', 'rel'],
                                 'dd': ['class', 'id', 'target', 'rel'], 'div': ['class', 'id', 'target', 'rel', 'style'],
                                 'dl': ['class', 'id', 'target', 'rel'], 'dt': ['class', 'id', 'target', 'rel'],
                                 'em': ['class', 'id', 'target', 'rel'], 'figcaption': ['class', 'id', 'target', 'rel'],
                                 'figure': ['class', 'id', 'target', 'rel'], 'h1': ['class', 'id', 'target', 'rel'],
                                 'h2': ['class', 'id', 'target', 'rel'], 'h3': ['class', 'id', 'target', 'rel'],
                                 'h4': ['class', 'id', 'target', 'rel'], 'h5': ['class', 'id', 'target', 'rel'],
                                 'h6': ['class', 'id', 'target', 'rel'], 'hr': ['class', 'id', 'target', 'rel'],
                                 'i': ['class', 'id', 'target', 'rel'],
                                 'img': ['class', 'id', 'target', 'rel', 'src', 'alt'],
                                 'li': ['class', 'id', 'target', 'rel'], 'ol': ['class', 'id', 'target', 'rel'],
                                 'p': ['class', 'id', 'target', 'rel'], 'pre': ['class', 'id', 'target', 'rel'],
                                 'span': ['class', 'id', 'target', 'rel'], 'strong': ['class', 'id', 'target', 'rel'],
                                 'sup': ['class', 'id', 'target', 'rel'], 'table': ['class', 'id', 'target', 'rel'],
                                 'tbody': ['class', 'id', 'target', 'rel'], 'td': ['class', 'id', 'target', 'rel'],
                                 'th': ['class', 'id', 'target', 'rel'], 'thead': ['class', 'id', 'target', 'rel'],
                                 'tr': ['class', 'id', 'target', 'rel'], 'ul': ['class', 'id', 'target', 'rel']}

WIKI_METHODS = ('article_list', 'toc', 'wikilinks')