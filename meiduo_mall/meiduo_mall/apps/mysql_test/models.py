from django.db import models


class UserTest(models.Model):
    """定义一个连接mysql的模型类"""

    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40)
    sex = models.CharField(max_length=10)
    birthday = models.DateField(verbose_name='出生日期')
    address = models.CharField(max_length=40)

    class Meta:
        # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        db_table = 'tb_user_test'  # 自定义表名
        # admin前端显示的表名称
        verbose_name = '用户测试表'
        verbose_name_plural = verbose_name

        # 联合唯一索引, # 应为两个存在的字段
        unique_together = (('username', 'address'),)

    def __str__(self):
        return f'姓名:{self.username},性别:{self.sex},生日:{self.birthday},地址:{self.address}'
