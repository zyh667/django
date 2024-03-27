from django.db import models

# Create your models here.
from django.db import models
from django.db.models import ImageField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.
class user_table(models.Model):
    studentID=models.CharField(max_length=20,verbose_name="学号",primary_key=True)
    sname=models.CharField(max_length=20,verbose_name="姓名")
    sex=models.CharField(max_length=10,verbose_name="姓别")
    password=models.CharField(max_length=100,default='123456',verbose_name="密码")
    phone=models.CharField(max_length=20,null=True,verbose_name="手机号")
    avatar=ImageField(upload_to='avatar',
                               default='avatar/111.jpg',
                               verbose_name='头像',)
    face_image=ImageField(upload_to='faceid/faces_from_camera',
                               default='无人脸信息',
                               verbose_name='人脸信息',)
    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'
    def __str__(self):
        return self.sname
class dormitory_form(models.Model):
    area = models.CharField(max_length=20,verbose_name="区域")
    build = models.CharField(max_length=20,verbose_name="楼号")
    floor = models.CharField(max_length=20,verbose_name="层数")
    number = models.CharField(max_length=20,verbose_name="房间号")
    residency = models.CharField(max_length=20)
    class Meta:
        unique_together=('area','build','floor','number')
class dormitory_table(models.Model):
    studentID = models.CharField(max_length=20,verbose_name="学号",primary_key=True)
    sname=models.CharField(max_length=20,verbose_name="姓名")
    area = models.CharField(max_length=20,verbose_name="区域")
    build = models.CharField(max_length=20,verbose_name="楼号")
    floor = models.CharField(max_length=20,verbose_name="层数")
    number = models.CharField(max_length=20,verbose_name="房间号")
    class Meta:
        verbose_name='宿舍管理'
        verbose_name_plural = '宿舍管理'
    def __str__(self):
        return self.studentID
class Repair_report_table(models.Model):
    area = models.CharField(max_length=20, verbose_name="区域")
    build = models.CharField(max_length=20, verbose_name="楼号")
    floor = models.CharField(max_length=20, verbose_name="层数")
    number = models.CharField(max_length=20, verbose_name="房间号")
    title = models.CharField(max_length=20,verbose_name="标题")
    content = models.CharField(max_length=100,verbose_name="内容")
    repair_status=models.CharField(max_length=20,default='未维修',verbose_name="维修情况")
    class Meta:
        verbose_name = '维修管理'
        verbose_name_plural = '维修管理'
class water_table(models.Model):
    area = models.CharField(max_length=20, verbose_name="区域")
    build = models.CharField(max_length=20, verbose_name="楼号")
    floor = models.CharField(max_length=20, verbose_name="层数")
    number = models.CharField(max_length=20, verbose_name="房间号")
    water = models.CharField(max_length=20,verbose_name="用水量")
    time = models.CharField(max_length=20,verbose_name="时间")
    status = models.CharField(max_length=20,default='未缴费',verbose_name="缴费情况")
    class Meta:
        verbose_name = '水费管理'
        verbose_name_plural = '水费管理'
    def __str__(self):
        return self.water
class electric_table(models.Model):
    area = models.CharField(max_length=20, verbose_name="区域")
    build = models.CharField(max_length=20, verbose_name="楼号")
    floor = models.CharField(max_length=20, verbose_name="层数")
    number = models.CharField(max_length=20, verbose_name="房间号")
    electric = models.CharField(max_length=20,verbose_name="用电量")
    time = models.CharField(max_length=20,verbose_name="时间")
    status = models.CharField(max_length=20,default='未缴费',verbose_name="缴费情况")
    class Meta:
        verbose_name = '电费管理'
        verbose_name_plural = '电费管理'
    def __str__(self):
        return self.electric
class tuition_table(models.Model):
    studentID = models.CharField(max_length=20,verbose_name='学号',primary_key=True)
    sname = models.CharField(max_length=20,verbose_name='姓名')
    tuition = models.CharField(max_length=20,verbose_name='学费')
    tuition_status = models.CharField(max_length=20,verbose_name='学费缴费情况')
    accommodation = models.CharField(max_length=20,verbose_name='住宿费')
    accommodation_status = models.CharField(max_length=20,verbose_name='住宿费缴费情况')
    class Meta:
        verbose_name = '学杂费管理'
        verbose_name_plural = '学杂费管理'
    def __str__(self):
        return self.studentID
class faces_record(models.Model):
    studentID = models.CharField(max_length=20,verbose_name='学号')
    time=models.CharField(max_length=100,verbose_name='时间')
    record=ImageField(upload_to='faceid/faces_record',verbose_name='门禁截图',)
    class Meta:
        verbose_name = '门禁记录'
        verbose_name_plural = '门禁记录管理'
    def __str__(self):
        return self.studentID