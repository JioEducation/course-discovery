import warnings
from os import environ

import certifi
import MySQLdb
import yaml

from course_discovery.settings.base import *
from course_discovery.settings.utils import get_env_setting

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

LOGGING['handlers']['local']['level'] = 'INFO'

# Keep track of the names of settings that represent dicts. Instead of overriding the values in base.py,
# the values read from disk should UPDATE the pre-configured dicts.
DICT_UPDATE_KEYS = (
    'COURSES_API_URL',
    'DATABASES'
    'EDX_DRF_EXTENSIONS',
    'JWT_AUTH',
    'SOCIAL_AUTH_EDX_OIDC_KEY',
    'SOCIAL_AUTH_EDX_OIDC_SECRET',
    'SOCIAL_AUTH_EDX_OIDC_URL_ROOT',
    'SOCIAL_AUTH_EDX_OIDC_ID_TOKEN_DECRYPTION_KEY',
)

CONFIG_FILE = get_env_setting('COURSE_DISCOVERY_CFG')

# Rjio fix , added setting overiding support from yml file
# Note: In case of dictonary keys should be defined in yml file.
if CONFIG_FILE:
    with open(CONFIG_FILE) as f:
        config_from_yaml = yaml.load(f)

        # Remove the items that should be used to update dicts, and apply them separately rather
        # than pumping them into the local vars.
        dict_updates = {key: config_from_yaml.pop(key, None) for key in DICT_UPDATE_KEYS}

        for key, value in dict_updates.items():
            if value:
                # Rjio override values from yml file
                vars()[key] = value

        vars().update(config_from_yaml)

# Rjio DB settings are loaded from the config file
DB_OVERRIDES = dict(
    PASSWORD=environ.get('DB_MIGRATION_PASS', DATABASES['default']['PASSWORD']),
    ENGINE=environ.get('DB_MIGRATION_ENGINE', DATABASES['default']['ENGINE']),
    USER=environ.get('DB_MIGRATION_USER', DATABASES['default']['USER']),
    NAME=environ.get('DB_MIGRATION_NAME', DATABASES['default']['NAME']),
    HOST=environ.get('DB_MIGRATION_HOST', DATABASES['default']['HOST']),
    PORT=environ.get('DB_MIGRATION_PORT', DATABASES['default']['PORT']),
)

# Rjio fix
ELASTICSEARCH_URL = "http://localhost:9200/"
ELASTICSEARCH_INDEX_NAME = "catalog"

HAYSTACK_CONNECTIONS['default'].update({
    'URL': ELASTICSEARCH_URL,
    'INDEX_NAME': ELASTICSEARCH_INDEX_NAME,
    'KWARGS': {
        'verify_certs': True,
        'ca_certs': certifi.where(),
    },
})

for override, value in DB_OVERRIDES.items():
    DATABASES['default'][override] = value

# NOTE (CCB): Treat all MySQL warnings as exceptions. This is especially
# desired for truncation warnings, which hide potential data integrity issues.
warnings.filterwarnings('error', category=MySQLdb.Warning)
