# Generated by Django 2.2.3 on 2019-07-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thegram', '0003_auto_20190728_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
