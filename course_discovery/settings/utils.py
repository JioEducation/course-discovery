from os import environ

from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or raise exception """
    try:
        # Rjio setting is obtained with get method
        return environ.get(setting, None)
    except KeyError:
        error_msg = "Set the [{}] env variable!".format(setting)
        raise ImproperlyConfigured(error_msg)
