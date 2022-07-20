from django.core.exceptions import ValidationError
from moviepy.video.io.VideoFileClip import VideoFileClip

import os
import subprocess

from moviepy.config import get_setting

# validating size and length of video 

def validate_file_size(value):
   
    filesize= value.size
    
    
    if filesize > 1073741824:
        raise ValidationError("The maximum file size that can be uploaded is 1 GB")
    else:
        return value
    


def validate_file_length(value):
    video_file_clip = VideoFileClip(value.temporary_file_path())
    video_duration = video_file_clip.duration
    
    
    if video_duration > 600:
        raise ValidationError("The maximum file length that can be uploaded is 10 minutes")
    else:
        return value

    