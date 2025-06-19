from django.db import models

# Create your models here.
# 模型层，实体类层
class User(models.Model):
    # 设置所需要映射的数据表，默认映射的表名是：应用名_全小写类名
    class Meta:
        db_table = "user"
 
    ISDEL_CHOICES = (
        (0, "未删除"),
        (1, "已删除")
    )
 
    # Django自带id字段，无需手动添加
    # id = models.IntegerField()
    # 将变量与数据库表字段进行映射，CharField限制该字段为字符串类型，限制该字段的长度、默认值，verbose_name字段注释
    name = models.CharField(max_length=20, default="", verbose_name="姓名")
    account = models.CharField(max_length=20, default="", verbose_name="账号")
    password = models.CharField(max_length=16, default="", null=False, verbose_name="密码")
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    # choices限制字段的取值范围，只能是0和1，只是形式上限制，实际执行user.del=2时并不会报错，可以正常插入到数据库
    isdel = models.IntegerField(null=False, choices=ISDEL_CHOICES)