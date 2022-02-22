from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password


# 使用信号拦截添加用户事件，加密口令
@receiver(pre_save)
def filter_user(sender, **kwargs):
    cls_class = str(sender) # <class user.models.UserModel>
    if cls_class.find('UserModel') > -1:
        obj = kwargs.get('instance') # UserModel类对象

        # 获取口令信息
        if len(obj.auth_key) < 50:
            # 是明文，需要加密
            obj.auth_key = make_password(obj.auth_key)
