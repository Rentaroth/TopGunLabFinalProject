import os
from dotenv import load_dotenv
load_dotenv()

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TGLBlog.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('TGLBlog', broker=os.getenv('REDIS_URI'))

app.conf.result_backend = os.getenv('REDIS_URI')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(CELERY_IMPORTS = (
  'app.tasks',
  'app.repositories.base_repository',
  'app.repositories.user_repository',
  'app.utilities.country_data',
))
app.conf.beat_schedule = {
    'my-periodic-task': {
        'task': 'app.utilities.country_data.periodic_country_api_call',
        'schedule': 3600,  # Intervalo de tiempo entre ejecuciones
        'options': {'expires': 60}
    },
}

def on_failure(exc, task_id, args, kwargs, einfo):
  return print({'task_id': task_id, 'message': einfo})

app.conf.task_on_failure = on_failure

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
  

if __name__ == '__main__':
  app.start()