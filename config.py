# config.py

class BaseConfiguration(object):
  DEBUG = False
  SECRET_KEY = ''

  CELERY_BROKER_URL = 'amqp://localhost:5672/0'
  CELERY_RESULT_BACKEND = 'amqp://localhost:5672/0'

