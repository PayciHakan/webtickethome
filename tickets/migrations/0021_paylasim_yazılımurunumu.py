# Generated by Django 4.0.4 on 2022-06-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0020_ariza_timestamp_ariza_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='paylasim',
            name='yazılımUrunumu',
            field=models.BooleanField(default=False),
        ),
    ]
