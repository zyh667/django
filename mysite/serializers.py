from rest_framework import serializers
from .models import *
class DormitorySerializers(serializers.ModelSerializer):
    class Meta:
        model=dormitory_table
        fields='__all__'
class Dormitory_from_Serializers(serializers.ModelSerializer):
    class Meta:
        model=dormitory_form
        fields='__all__'
class WaterSerializers(serializers.ModelSerializer):
    class Meta:
        model=water_table
        fields='__all__'
class RepairSerializers(serializers.ModelSerializer):
    class Meta:
        model=Repair_report_table
        fields='__all__'
class ElectricSerializers(serializers.ModelSerializer):
    class Meta:
        model=electric_table
        fields='__all__'
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=user_table
        fields='__all__'
class TuitionSerializers(serializers.ModelSerializer):
    class Meta:
        model=tuition_table
        fields='__all__'
class RecordSerializers(serializers.ModelSerializer):
    class Meta:
        model=faces_record
        fields='__all__'