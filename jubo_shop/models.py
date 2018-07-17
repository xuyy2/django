from django.db import models


# Create your models here
# class ClerkManager(models.Model):
#     def create_clerk(self, name, join_time, is_available):
#         clerk = self.create_clerk(
#             name=name, join_time=join_time, is_available=True)
#         return clerk


class Clerk(models.Model):
    """
    员工表
    """
    # 名字
    name = models.CharField(verbose_name='姓名', max_length=20)
    # 加入时间
    join_time = models.DateTimeField(verbose_name='入职时间', auto_now_add=True)
    # 是否可用
    is_available = models.NullBooleanField(verbose_name='是否可用')
    # clerk = ClerkManager()

    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工'

    def __str__(self):
        return self.name


class Counter(models.Model):
    """
    货柜
    """
    # 序列号
    serial_number = models.CharField(verbose_name='序列号', max_length=20)
    # 地址
    address = models.CharField(verbose_name='地址', max_length=20)
    # 负责人
    clerk = models.ForeignKey(Clerk, verbose_name='上货员')

    class Meta:
        verbose_name = '货柜'
        verbose_name_plural = '货柜'

    def __str__(self):
        return self.serial_number


class AddGoods(models.Model):
    """
    添加商品
    """
    # 商品名称
    name = models.CharField(verbose_name='商品名称', max_length=20)
    # 商品数量
    number = models.IntegerField(verbose_name='数量')
    # 创建时间
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 添加人员
    clerk = models.ForeignKey(Clerk, verbose_name='上货员')
    # 货柜
    counter = models.ForeignKey(Counter, verbose_name='所属货柜')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'

    def __str__(self):
        return self.name
