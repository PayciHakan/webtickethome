# Generated by Django 4.0.4 on 2022-06-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0026_rename_timestamp_ariza_create_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paylasim',
            name='sssmi',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='paylasim',
            name='gönderiDurumu',
            field=models.BooleanField(default=True),
        ),
    ]
