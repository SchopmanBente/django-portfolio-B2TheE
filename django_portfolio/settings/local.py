import json
import os.path
from django.core.exceptions import ImproperlyConfigured


path = 'django_portfolio/settings/secrets.json'
os_path = os.path.realpath(path)
os_path_string = str(os_path)
json_data = ''.join([os_path_string])
#data = open(json_data,'f')
with open(json_data,'r') as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0) environment variable".format(setting)
        raise  ImproperlyConfigured(error_msg)
