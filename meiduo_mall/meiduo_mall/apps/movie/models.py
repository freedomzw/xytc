from django.db import models


# Create your models here.

class test(models.Model):
    name = models.CharField(max_length=13, verbose_name="姓名")
    addr = models.CharField(max_length=20, verbose_name="地址")

    class Meta:
        db_table = 'test'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称


class test2(models.Model):
    name = models.CharField(max_length=20, verbose_name="名字")
    gender = models.BooleanField()
    book = models.ForeignKey(test, on_delete=models.CASCADE)

    class Meta:
        db_table = 'test2'
        verbose_name = '人物信息'


class emp(models.Model):
    name = models.CharField(max_length=30, verbose_name="员工姓名")
    age = models.IntegerField(verbose_name="员工年龄")
    dep_name = models.CharField(max_length=30, verbose_name="部门名称")
    dep_location = models.CharField(max_length=30, verbose_name="部门位置")

    class Meta:
        db_table = 'emp'
        verbose_name = '员工信息'

    def __str__(self):
        return self.name


class department(models.Model):
    dep_name = models.CharField(verbose_name='部门名称', max_length=20)
    dep_location = models.CharField(verbose_name='部门名称', max_length=20)

    class Meta:
        db_table = 'department'
        verbose_name = '部门'


class employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(verbose_name="年龄")
    dep_id = models.IntegerField(verbose_name="部门id")

    class Meta:
        db_table = 'employee'
        verbose_name = '员工'
