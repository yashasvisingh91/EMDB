# Generated by Django 2.0.1 on 2018-02-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0004_auto_20180205_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
    ]
