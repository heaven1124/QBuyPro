from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app
import pymysql


# 向项目模块中增加celery_app对象
__all__ = ('celery_app',)

pymysql.install_as_MySQLdb()







