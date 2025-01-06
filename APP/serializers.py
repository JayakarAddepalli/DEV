from rest_framework import serializers
from .models import *

class PythonBlogsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonBlogsModel
        fields = '__all__'

class HTMLBlogsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HTMLBlogsModel
        fields = '__all__'

class CSSBlogsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSSBlogsModel
        fields = '__all__'