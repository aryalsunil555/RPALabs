from rest_framework import serializers


from video.models import VideoTab


class VideoTabSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = VideoTab
        fields = ['title','video','description','date_uploaded']