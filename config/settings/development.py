from .base import *
import os

DEBUG = os.getenv("DEBUG_DEV") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS_DEV").split(",")

DATABASES = {
    'default': {
        'ENGINE': os.getenv("DB_ENGINE_DEV"),
        'NAME':  os.getenv("DB_NAME_DEV"),
    }
}
