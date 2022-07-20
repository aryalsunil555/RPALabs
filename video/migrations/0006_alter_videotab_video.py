# Generated by Django 4.0.6 on 2022-07-20 09:39

import django.core.validators
from django.db import migrations, models
import video.validators


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_rename_charge_videotab_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videotab',
            name='video',
            field=models.FileField(null=True, upload_to='video_uploads/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mkv']), video.validators.validate_file_size, video.validators.validate_file_length]),
        ),
    ]
