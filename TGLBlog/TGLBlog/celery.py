import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TGLBlog.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('TGLBlog', broker='redis://default:7SBuxGsqDzXqqIQbQI9rV7fwoxeo2AhF@redis-13641.c61.us-east-1-3.ec2.cloud.redislabs.com:13641')

app.conf.result_backend = 'redis://default:7SBuxGsqDzXqqIQbQI9rV7fwoxeo2AhF@redis-13641.c61.us-east-1-3.ec2.cloud.redislabs.com:13641'
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(CELERY_IMPORTS = (
  'app.tasks',
  'app.repositories.base_repository',
))

def on_failure(exc, task_id, args, kwargs, einfo):
  return print({'task_id': task_id, 'message': einfo})

app.conf.task_on_failure = on_failure

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
  

if __name__ == '__main__':
  app.start()