import os


class Config(object):
  SECRET_KY = os.environ.get('SECRECT_KEY') or "secret_string"