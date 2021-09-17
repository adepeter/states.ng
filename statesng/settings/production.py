import os

from .base import *

DEBUG = False
ALLOWED_HOSTS = os.environ.get('STATES_NG_HOST')
