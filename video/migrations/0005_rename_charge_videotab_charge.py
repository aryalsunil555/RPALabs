# Generated by Django 4.0.6 on 2022-07-20 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_videotab_charge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videotab',
            old_name='Charge',
            new_name='charge',
        ),
    ]
