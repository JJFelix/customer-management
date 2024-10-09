"""
Django settings for customer_management project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

from dotenv import load_dotenv, find_dotenv
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIR = os.path.join(BASE_DIR, "customers", "templates")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")


# Application definition

INSTALLED_APPS = [
    # "jazzmin",
    "customers.apps.CustomersConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',

]

ROOT_URLCONF = 'customer_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'customer_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST', default='localhost'),
#         'PORT': os.getenv('DB_PORT', default='5432'),
#     }
# }
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        # conn_max_age=600
    )
}

if os.getenv('GITHUB_ACTIONS'):
    DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
        }
    } 

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# OAUTH2_PROVIDER = {
#     "OICD_ENABLED": True,
#     "OIDC_RSA_PRIVATE_KEY": os.getenv('OIDC_RSA_PRIVATE_KEY'),
#     "OIDC_RP_INITIATED_LOGOUT_ENABLED": True,
#     "OIDC_RP_INITIATED_LOGOUT_ALWAYS_PROMPT": True,
#     "SCOPES": {
#         "openid": "OpenID Connect scope",
#     },
#     "OAUTH2_VALIDATOR_CLASS": "customer_management.oauth_validators.CustomOAuth2Validator",
# }

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://customer-management-client.onrender.com",
    "https://customer-management-api-grx3.onrender.com",
]

CORS_ALLOW_CREDENTIALS = True

# CORS_ORIGIN_WHITELIST = [
#     "http://localhost:5173"
# ]

# CORS_ALLOW_ALL_ORIGINS = True

# Africa's talking
AFRICAS_TALKING_USERNAME = os.getenv("AFRICAS_TALKING_USERNAME")
AFRICAS_TALKING_API_KEY = os.getenv("AFRICAS_TALKING_API_KEY")
AFRICAS_TALKING_SENDER_CODE = os.getenv("AFRICAS_TALKING_SENDER_CODE")
