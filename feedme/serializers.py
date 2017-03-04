from .models import *
from rest_framework import serializers

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = video
        fields = ('title', 'created', 'instruction', 'price', 'rating', 'view_count')