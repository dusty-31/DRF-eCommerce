from drfecommerce.settings import base

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': base.BASE_DIR / 'db.sqlite3',
    }
}
