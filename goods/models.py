from django.db import models

# Create your models here.


class Goods(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='名称')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='单价')
    info = models.TextField(verbose_name='商品描述')
    img1 = models.ImageField(verbose_name='图片1',
                             upload_to='goods')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_goods'
        verbose_name_plural = verbose_name = '商品信息'

