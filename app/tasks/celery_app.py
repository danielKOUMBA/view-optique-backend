from celery import Celery
import os 
from app.Config import Config
def make_celery(app):
    celery=Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_BACKEND_RESULT']
    )

    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self,*args,**kwargs):
            with app.app_context():
                return self.run(*args,**kwargs)
    celery.Task=ContextTask

    return celery

def init_celery(celery,app):
    celery.conf.update(app.config)

    celery.autodiscover_tasks([
           'app.tasks'
    ])
        