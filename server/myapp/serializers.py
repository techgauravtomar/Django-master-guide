from rest_framework import serializers
from .models import StudentModel

class StudentSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=50)
    email=serializers.EmailField(max_length=50)
    password=serializers.CharField(max_length=30)
    confirm_pass=serializers.CharField(max_length=30)
    class Meta:
        model = StudentModel
        fields = "__all__"