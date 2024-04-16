[# unittest在django中的使用

```
#执行项目中所有以test开头的py文件都会被执行
python manage.py test

#运行某一个名为users的app下面的所有测试用例， users对应app_name,应用中所有app下额
的test用例
python manage.py test app01

#运行某一个名为users的app下面的所有测试用例，tests.py文件
python manage.py test app01.tests

#运行某一个名为users的app下面的所有测试用例文件夹中某一个文件
python manage.py test app01.testcase.test_basic2
#运行某一个名为users的app下面的所有测试用例文件夹中某一个文件中的某一个类
python manage.py test app01.testcase.test_basic1.TestStringMethods

如果是事务形操作的话需要继承TestCase中TransactionTestCase类
```
