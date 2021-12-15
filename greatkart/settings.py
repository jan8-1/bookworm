"""
Django settings for greatkart project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent





SECRET_KEY = '52$5ujr925j_8)+c4+yhwik_+vq6e13#fxi5**_$rv80pn3(sf'


DEBUG = True

ALLOWED_HOSTS = ['greatkart-course-env.eba-ptvtpukz.us-east-1.elasticbeanstalk.com','*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'category',
    'accounts',
    'store',
    'carts',
    'orders',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'greatkart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'carts.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'greatkart.wsgi.application'

AUTH_USER_MODEL = 'accounts.Account'




# Database connection
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'ebdb',
            'USER': 'greatkartuser',
            'PASSWORD': 'asdfghjkl123',
            # 'USER': 'janit',
            # 'PASSWORD': 'janit123',
            'HOST': 'aa1a1lozmtzk6n8.cl0pbpduwcnq.us-east-1.rds.amazonaws.com',
            'PORT': 5432,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': 'ebdb',
#             'USER': 'greatkartuser',
#             'PASSWORD': 'asdfghjkl123',
#             # 'USER': 'janit',
#             # 'PASSWORD': 'janit123',
#             'HOST': 'aa1a1lozmtzk6n8.cl0pbpduwcnq.us-east-1.rds.amazonaws.com',
#             'PORT': 5432,
#         }
#     }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'ebdb',
#         'USER': 'greatkartuser',
#         'PASSWORD': 'asdfghjkl13',
#         'HOST': 'aa1a1lozmtzk6n8.cl0pbpduwcnq.us-east-1.rds.amazonaws.com',
#         'PORT': 5432,
#     }
# }
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# aws s3 static file 
# -
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR /'static'
STATICFILES_DIRS = [
    'greatkart/static',
]

# AWS_ACCESS_KEY_ID = 'ASIAVK2NRDKZUWLNG653'
# AWS_SECRET_ACCESS_KEY = 'ZHC9bbNoVSZiNTmWQVGDl8Zk8iBWjVPUUyWaS1am'
# AWS_STORAGE_BUCKET_NAME = 'bookworm-s3'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = 'public-read'
# AWS_LOCATION = 'static'

# STATICFILES_DIRS = [
#     'greatkart/static',
# ]
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media'


from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# configration for email 
# SMTP configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'janitpathak@gmail.com'
EMAIL_HOST_PASSWORD = 'hacktsztthiyqnwy'
EMAIL_USE_TLS = True
