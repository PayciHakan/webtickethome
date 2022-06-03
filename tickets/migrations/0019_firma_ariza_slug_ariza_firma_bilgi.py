# Generated by Django 4.0.4 on 2022-06-02 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0018_alter_paylasim_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirmaName', models.CharField(default='Firmasız', max_length=100)),
                ('FirmaYetkilisi', models.CharField(max_length=50)),
                ('FirmaİletisimMail', models.CharField(max_length=50)),
                ('FirmaİletisimTelefon', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='ariza',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='ariza',
            name='firma_bilgi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.firma'),
        ),
    ]