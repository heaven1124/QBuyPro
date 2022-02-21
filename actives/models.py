from django.db import models

# Create your models here.
from goods.models import Goods


class Active(models.Model):
    title = models.CharField(max_length=20,
                             verbose_name='名称')
    img1 = models.ImageField(verbose_name='图片1',
                             upload_to='actives')
    start_time = models.CharField(max_length=30,
                                  verbose_name='开始时间')
    end_time = models.CharField(max_length=30,
                                verbose_name='结束时间')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_actives'
        verbose_name_plural = verbose_name = '活动信息'


class ActiveGoods(models.Model):
    active = models.ForeignKey(Active,
                               related_name='goods',
                               on_delete=models.SET_NULL,
                               null=True,
                               verbose_name='活动名')
    goods = models.ForeignKey(Goods,
                              related_name='actives',
                              on_delete=models.SET_NULL,
                              null=True,
                              verbose_name='商品名')
    rate = models.FloatField(verbose_name='折扣率',
                             default=.88)

    def __str__(self):
        return self.active.title + ":" + self.goods.name

    class Meta:
        db_table = 'app_active_goods'
        verbose_name_plural = verbose_name = '活动详情'


