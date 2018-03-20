import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'j*6-2j6hpvx^$(1sn6%%!df2ixe822wd!x#hm0s@ew$cnydqtr'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Gmail SMTP : www.codingforentrepreneurs.com/blog/use-gmail-for-email-in-django/
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'muyongcctv@gmail.com'
EMAIL_HOST_PASSWORD = 'homecctv$$'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
LOGIN_REDIRECT_URL = '/'   # '/accounts/login/' 기본 URL 경로

# CKEditor settings
# https://github.com/django-ckeditor/django-ckeditor
CKEDITOR_UPLOAD_PATH = "/static/uploads/"
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'full',
#         'height': 300,
#         'width' : 300,  },}

# Application definition
INSTALLED_APPS = [
    'ckeditor',          # HTML Editor
    'ckeditor_uploader', # HTML Editor Widget
    'django.contrib.admin',
    'django.contrib.auth',  # 사용자 관리
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'rest_framework',
    'blogs.apps.BlogsConfig',
    'stock.apps.StockConfig',
    'posts.apps.PostsConfig',
    'photo.apps.PhotoConfig',
    'tagging.apps.TaggingConfig',
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

ROOT_URLCONF = 'server.urls'
WSGI_APPLICATION = 'server.wsgi.application'
TEMPLATES = [
    {   'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static/templates')], # Master Templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
    ],},},]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'django.db'),
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME':'games',
        # 'USER':'quents',
        # 'PASSWORD':'erdos8989',
        # 'HOST':'127.0.0.1',
        # 'PORT':'5432',
}}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Seoul' #TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True