from celery import Celery

celery_app = Celery(
    'issues_insights_tracker',
    broker='redis://redis:6379/0',     # or your RabbitMQ if you use it
    backend='redis://redis:6379/0'      # optional, for result backend
)
celery_app.conf.update(
    task_routes = {
        # "myapp.tasks.*": {"queue": "important"},
    },
    timezone='UTC',
    enable_utc=True,
)
