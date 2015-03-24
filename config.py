# config.py

class BaseConfiguration(object):
  DEBUG = False
  SECRET_KEY = ''

  CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'
  CELERY_RESULT_BACKEND = 'amqp://guest:guest@localhost:5672//'
  CELERY_TASK_SERIALIZER = 'json'
  CELERY_ACCEPT_CONTENT = ['json']
