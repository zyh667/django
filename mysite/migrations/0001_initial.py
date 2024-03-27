# Generated by Django 2.2 on 2024-03-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dormitory_table',
            fields=[
                ('studentID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='学号')),
                ('sname', models.CharField(max_length=20, verbose_name='姓名')),
                ('area', models.CharField(max_length=20, verbose_name='区域')),
                ('build', models.CharField(max_length=20, verbose_name='楼号')),
                ('floor', models.CharField(max_length=20, verbose_name='层数')),
                ('number', models.CharField(max_length=20, verbose_name='房间号')),
            ],
            options={
                'verbose_name': '宿舍管理',
                'verbose_name_plural': '宿舍管理',
            },
        ),
        migrations.CreateModel(
            name='electric_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20, verbose_name='区域')),
                ('build', models.CharField(max_length=20, verbose_name='楼号')),
                ('floor', models.CharField(max_length=20, verbose_name='层数')),
                ('number', models.CharField(max_length=20, verbose_name='房间号')),
                ('electric', models.CharField(max_length=20, verbose_name='用电量')),
                ('time', models.CharField(max_length=20, verbose_name='时间')),
                ('status', models.CharField(default='未缴费', max_length=20, verbose_name='缴费情况')),
            ],
            options={
                'verbose_name': '电费管理',
                'verbose_name_plural': '电费管理',
            },
        ),
        migrations.CreateModel(
            name='faces_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.CharField(max_length=20, verbose_name='学号')),
                ('time', models.CharField(max_length=100, verbose_name='时间')),
                ('record', models.ImageField(upload_to='faceid/faces_record', verbose_name='门禁截图')),
            ],
            options={
                'verbose_name': '门禁记录',
                'verbose_name_plural': '门禁记录管理',
            },
        ),
        migrations.CreateModel(
            name='Repair_report_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20, verbose_name='区域')),
                ('build', models.CharField(max_length=20, verbose_name='楼号')),
                ('floor', models.CharField(max_length=20, verbose_name='层数')),
                ('number', models.CharField(max_length=20, verbose_name='房间号')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('content', models.CharField(max_length=100, verbose_name='内容')),
                ('repair_status', models.CharField(default='未维修', max_length=20, verbose_name='维修情况')),
            ],
            options={
                'verbose_name': '维修管理',
                'verbose_name_plural': '维修管理',
            },
        ),
        migrations.CreateModel(
            name='tuition_table',
            fields=[
                ('studentID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='学号')),
                ('sname', models.CharField(max_length=20, verbose_name='姓名')),
                ('tuition', models.CharField(max_length=20, verbose_name='学费')),
                ('tuition_status', models.CharField(max_length=20, verbose_name='学费缴费情况')),
                ('accommodation', models.CharField(max_length=20, verbose_name='住宿费')),
                ('accommodation_status', models.CharField(max_length=20, verbose_name='住宿费缴费情况')),
            ],
            options={
                'verbose_name': '学杂费管理',
                'verbose_name_plural': '学杂费管理',
            },
        ),
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('studentID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='学号')),
                ('sname', models.CharField(max_length=20, verbose_name='姓名')),
                ('sex', models.CharField(max_length=10, verbose_name='姓别')),
                ('password', models.CharField(default='123456', max_length=100, verbose_name='密码')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='手机号')),
                ('avatar', models.ImageField(default='avatar/111.jpg', upload_to='avatar', verbose_name='头像')),
                ('face_image', models.ImageField(default='无人脸信息', upload_to='faceid/faces_from_camera', verbose_name='人脸信息')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
            },
        ),
        migrations.CreateModel(
            name='water_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20, verbose_name='区域')),
                ('build', models.CharField(max_length=20, verbose_name='楼号')),
                ('floor', models.CharField(max_length=20, verbose_name='层数')),
                ('number', models.CharField(max_length=20, verbose_name='房间号')),
                ('water', models.CharField(max_length=20, verbose_name='用水量')),
                ('time', models.CharField(max_length=20, verbose_name='时间')),
                ('status', models.CharField(default='未缴费', max_length=20, verbose_name='缴费情况')),
            ],
            options={
                'verbose_name': '水费管理',
                'verbose_name_plural': '水费管理',
            },
        ),
        migrations.CreateModel(
            name='dormitory_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20, verbose_name='区域')),
                ('build', models.CharField(max_length=20, verbose_name='楼号')),
                ('floor', models.CharField(max_length=20, verbose_name='层数')),
                ('number', models.CharField(max_length=20, verbose_name='房间号')),
                ('residency', models.CharField(max_length=20)),
            ],
            options={
                'unique_together': {('area', 'build', 'floor', 'number')},
            },
        ),
    ]
