# Django Demo

## Goals

Expose learners to opinionated framework - this will help learners to tell the differences between opinionated and unopinionated framework based on experience.

## Quick Setup

Step 1: Setup environment

```sh
mkdir django-demo 
cd django-demo
python3 -m venv djangoenv
source ./djangoenv/bin/activate
pip install django
```

Step 2: Setup main project and app

```sh
django-admin startproject main
django-admin startapp api
```

Step 3: Change `default_port` from `8000` to `9000` (in `runserver.py` file).

Step 4: Test run default project

```sh
cd main
python manage.py runserver
```

Step 5: Add the commented line in `settings.py` within the `main` project folder.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig' # add this line
]
```

Step 6: In the same `settings.py` file, comment CSRF middleware

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

## Setup Database

Step 1: Install postgres adapter

```sh
pip install psycopg2
```

Step 2: Login to PG console and insert the following SQL Commands

```sql
CREATE DATABASE djangodb;
CREATE USER djangouser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE djangodb TO djangouser;
```

Step 3: Configure `settings.py` in main project

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb', 
        'USER': 'djangouser', 
        'PASSWORD': 'password',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
```

## Setup `rest_framework` module

Step 1: Install rest framework

```sh
pip install djangorestframework
```

Step 2: General a new app call `rest`

```sh
python manage.py startapp rest
```

Step 3: Add `rest_framework` to the `INSTALLEd_APPS` of `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'model.apps.ModelConfig',
    'rest.apps.RestConfig',
    'rest_framework'
]
```

## Setup JWT Authentication

Step 1: Install dependencies

```sh
pip install djangorestframework_simplejwt django_extensions
```

Step 2: Update `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'model.apps.ModelConfig',
    'rest.apps.RestConfig',
    'rest_framework',
    'django_extensions'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
```

Step 3: Add Serializers

See [serializers.py](./main/rest/serializers.py)

Step 4: Add `RegisterUsersView` Class

See [views.py](./main/rest/views.py)

Step 5: Update `urls.py` in the main project

See [urls.py](./main/main/urls.py)

Step 6: Update Permission for `EmployeeViewSet`

Modify this line `permission_classes = [permissions.IsAuthenticated]`

Now, the rest endpoints require `Authorization Bearer <token>`