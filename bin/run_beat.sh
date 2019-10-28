celery -A scheduOps beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
