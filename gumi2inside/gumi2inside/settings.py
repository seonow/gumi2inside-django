"""
Django settings for gumi2inside project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2mutif%q1ft7^z63i0)9*w_m@c#xu7ynrmb*4%(9a6uva_1-9x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ec2-54-180-115-105.ap-northeast-2.compute.amazonaws.com',
                 'gumi2inside.site',
                 'localhost','*']


# Application definition

INSTALLED_APPS = [
    'announcements',
    'articles',
    'ciders',
    'accounts',
    'rboards',
    'storages',
    'admin_img',
    'rest_framework',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'gumi2inside.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'gumi2inside.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True
USE_L10N = True 
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
] #static 파일들이 어디에 있는지를 쓰는곳


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CSRF_TRUSTED_ORIGINS = ['https://gumi2inside.site']

# 일단 비활성화
# CSRF_COOKIE_SECURE = True  # CSRF 쿠키는 HTTPS를 통해서만 전송됩니다.
# CSRF_COOKIE_HTTPONLY = True  # 자바스크립트에서 CSRF 쿠키에 접근할 수 없습니다.
# DEBUG = False

# GPT 말
# CSRF_COOKIE_SECURE:
# 이 설정을 True로 하면, CSRF 쿠키는 HTTPS를 통해서만 전송됩니다. 즉, 암호화되지 않은 HTTP 연결을 통해서는 쿠키가 전송되지 않게 됩니다. 이렇게 하면 중간자 공격(man-in-the-middle attacks)을 통한 쿠키 탈취를 어렵게 만듭니다.
# 만약 당신의 웹사이트가 HTTPS를 지원한다면 이 설정을 활성화하는 것이 좋습니다.

# CSRF_COOKIE_HTTPONLY:
# 이 설정을 True로 하면, 자바스크립트를 통해 CSRF 쿠키에 접근하는 것이 불가능해집니다. 이는 크로스 사이트 스크립팅 공격(XSS attacks)을 통해 쿠키가 탈취되는 것을 방지하는 데 도움을 줍니다.
# 웹사이트에 자바스크립트를 통해 CSRF 쿠키에 접근할 필요가 없다면 이 설정을 활성화하는 것이 좋습니다.

AUTH_USER_MODEL = 'accounts.User'

### upload
AWS_ACCESS_KEY_ID = 'AKIAROL4U6BLURACMOF5'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'gumi2inside'
AWS_S3_REGION_NAME = 'ap-northeast-2' 

# 정적 파일 및 미디어 파일을 저장할 S3 경로 설정
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_URL_PROTOCOL = 'https'

# 정적 파일 저장 위치 설정
STATIC_URL = f'{AWS_S3_URL_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# 미디어 파일 저장 위치 설정
MEDIA_URL = f'{AWS_S3_URL_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/media/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
