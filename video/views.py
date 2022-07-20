from django import forms
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import VideoTab
from moviepy.video.io.VideoFileClip import VideoFileClip

from video.serializers import VideoTabSerializer

# Add video To Database



class AddVideoView(APIView):
    

    def post(self, request, format=None):

        
        serializer = VideoTabSerializer(data=request.data)
        
        if serializer.is_valid():

            vid_size = serializer.validated_data.get('video')
            video_file_clip = VideoFileClip(vid_size.temporary_file_path())
            video_duration = video_file_clip.duration

            if vid_size.size < 524288000 and video_duration < 378:
                
                vid_charge = 17.5
            elif vid_size.size < 524288000 and video_duration > 378:
                vid_charge = 20
            
            elif vid_size.size > 524288000 and video_duration < 378:
                vid_charge = 25
            else:

                vid_charge = 32.5
            
            serializer.save(charge=vid_charge)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Browse all uploaded videos


class BrowseVideos(generics.ListAPIView):
    
    serializer_class = VideoTabSerializer

    def get_queryset(self):
        
        
        allvideo = VideoTab.objects.all()
        return allvideo.order_by('-date_uploaded')