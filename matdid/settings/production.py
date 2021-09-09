from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["matdid-back-end.herokuapp.com"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'df1ncqb8s60um7',
        'USER': 'hycyzahhoirzvi',
        'PASSWORD': '28b483d4530317f699d8fe79f2eb33b4cc99ba6f3d8dfc9844f18cc01ea987c3',
        'HOST': 'ec2-52-0-93-3.compute-1.amazonaws.com',
        'PORT': 5432
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'