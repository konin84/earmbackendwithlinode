from rest_framework import serializers
#   from rest_framework.validators import ValidationError

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'