from datetime import timezone
from django.core.validators import FileExtensionValidator
from django.db import models
from .validators import validate_file_size, validate_file_length

# creating Table to store Video Data

class VideoTab(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='video_uploads/',null=True,
            validators=[FileExtensionValidator(allowed_extensions=['mp4','mkv']),validate_file_size, validate_file_length])
    date_uploaded = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    charge = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        ordering = ['-date_uploaded']
    def __str__(self):
        return self.title