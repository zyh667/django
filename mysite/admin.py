from django.contrib import admin

# Register your models here.
from mysite.models import *

admin.site.site_header = '学宿通后台管理'
admin.site.site_title = '宿舍管理'
admin.site.index_title = '校园管理'
@admin.register(user_table)
class userAdmin(admin.ModelAdmin):
    # 列表界面的自定义
    list_display = ('studentID','sname','sex','password','phone','avatar','face_image')
    list_display_links = ('sname',)  # 设置字段链接
@admin.register(dormitory_table)
class dorAdmin(admin.ModelAdmin):
    list_display = ('studentID','sname','area','build','floor','number')
@admin.register(Repair_report_table)
class Repair_report_tableAdmin(admin.ModelAdmin):
    list_display = ('title','content','repair_status')
@admin.register(water_table)
class water_tableAdmin(admin.ModelAdmin):
    list_display = ('area','build','floor','number','water','time','status')
@admin.register(electric_table)
class electric_tableAdmin(admin.ModelAdmin):
    list_display = ('area', 'build', 'floor', 'number','electric','time', 'status')
@admin.register(tuition_table)
class tuition_tableAdmin(admin.ModelAdmin):
    list_display = ('studentID', 'sname', 'tuition','tuition_status','accommodation','accommodation_status')
@admin.register(faces_record)
class faces_recordAdmin(admin.ModelAdmin):
    list_display = ('studentID', 'time','record')