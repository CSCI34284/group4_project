"""

Prepared by Backend/Server Team - Sheldon, Martin, Brian, Veronica, Sarah with input from front-end team for configuration purposes (Yilin/Kretish/Rafid/Gauthum/Lulu).
"""

import os
import mimetypes

mimetypes.add_type("text/css", ".css", True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '9nneu#^7_aai*(#(6_qiihu-^k-+%a86&vjh=_i9#(c4^8s51n'
DEBUG = True
ALLOWED_HOSTS = ['ugdev.cs.smu.ca', '140.184.230.209', '140.184.230.226', 'localhost', '127.0.0.1', '192.168.2.12']

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'corsheaders',
    'channels',
    'rest_auth',
    'rest_auth.registration',
    'rest_framework',
    'rest_framework.authtoken',

    'chat'
]

# Middleware configuration
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'smumessaging.urls'

# Frontend template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'smumessaging.wsgi.application'
ASGI_APPLICATION = "smumessaging.routing.application"

# Redis configuration
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('140.184.230.209', 6379)],
        },
    },
}

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'sd_taylor',
#        'USER': 'sd_taylor',
#        'PASSWORD': 'A00359986',
#        'HOST': '140.184.230.209',
#        'PORT': '3306',
#    }        
#}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', }
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Staticfiles configuration
STATIC_URL = '/static/'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'build/static'), os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_ROOT = '/static/'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Authentication settings
SITE_ID = 1
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# Frontend/Backend configuration
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:5000',
    'http://localhost:8000',
    'http://localhost:8080',
    'http://192.168.2.12:3000',
    'http://192.168.2.12:5000',
    'http://192.168.2.12:8000',
    'http://192.168.2.12:8080',
    'http://140.184.230.226:3000',
    'http://140.184.230.226:5000',
    'http://140.184.230.226:8000',
    'http://140.184.230.226:8080',
    'http://140.184.230.209:3080',
    'http://140.184.230.209:5080',
    'http://140.184.230.209:8000',
    'http://140.184.230.209:8080',
    'http://ugdev.cs.smu.ca:3000',
    'http://ugdev.cs.smu.ca:5000',
    'http://ugdev.cs.smu.ca:8000',
    'http://ugdev.cs.smu.ca:8080'
]

ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'none'
CSRF_COOKIE_NAME = "csrftoken"

# Host configuration
HOST_URL = 'http://140.184.230.209:8000'
if DEBUG:
    #HOST_URL = 'http://127.0.0.1:8000'
    HOST_URL = 'http://140.184.230.209:8000'
