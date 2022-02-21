from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'QBuyPro.settings')
app = Celery('QBuyPro',
             broker='redis://:123@10.0.0.48:6379/3',
             backend='redis://:123@10.0.0.48:6379/4',
             namespace='Celery')
app.config_from_object('django.conf:settings') # 配置Celery,加载settings.py文件

app.autodiscover_tasks() # 自动发现task任务

