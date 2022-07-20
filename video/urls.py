
from django.contrib import admin
from django.urls import include, path,re_path

from video.views import AddVideoView, BrowseVideos
from video import views


urlpatterns = [
   
    re_path('add_video/', AddVideoView.as_view(), name="addvideo"),
    re_path('all_videos/', BrowseVideos.as_view(), name="allvideos"),
   
]