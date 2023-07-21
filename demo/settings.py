

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%&g*d$+m388s#gv27w$4ij2_hw_p3+r06t66)zbnvv20fgvvkp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS=[
        # "https://web-production-07f6.up.railway.app",
    "https://rba-production.up.railway.app"
    ]
# CORS_ALLOWED_ORIGINS = [
#         # "https://web-production-07f6.up.railway.app",
#         "https://rba-production.up.railway.app/",
#         # Add other allowed origins here if needed
#     ]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
       "whitenoise.runserver_nostatic",
       'corsheaders',
   
    
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'users.middleware.GetClientIPMiddleware',

]
# E:\final ieee\test\demo\users\middleware.py
ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',
        'NAME': 'railway',
        'USER': 'root',
        'PASSWORD':'xPQpGkaAI6YVBPdxWmmC',
        'HOST':'containers-us-west-115.railway.app',
        'PORT':'6837',
          'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'db_iee',  # The name of your PostgreSQL database
#         'USER': 'root',    # The PostgreSQL username
#         'PASSWORD': 'w2Ol2HodHNiS8v3LSyZwOZ0w3HXeQspx',  # The PostgreSQL password
#         'HOST': 'dpg-cir6madgkuvqadovbdrg-a.singapore-postgres.render.com',  # The external host provided by Render
#         'PORT': '5432',    # The PostgreSQL port number (default is usually 5432)
#     }
# }



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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# STATIC_HOST = "https://web-production-07f6.up.railway.app/" if not DEBUG else ""
# # STATIC_URL = STATIC_HOST + "/static/"
# STATIC_URL = '/staticfiles'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# VENV_PATH = os.path.dirname(BASE_DIR)
# STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'home'

STATIC_HOST = "https://web-production-07f6.up.railway.app/" if not DEBUG else ""
STATIC_URL = STATIC_HOST + "/static/"
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
VENV_PATH = os.path.dirname(BASE_DIR)
# STATIC_ROOT = '/home/eihy0p9s0spe/public_html/rba/rbastatic'
# STATIC_ROOT = '/rbastatic/'

STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')



STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
