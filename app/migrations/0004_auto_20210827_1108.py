# Generated by Django 3.1.7 on 2021-08-27 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210826_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(default=True, upload_to='book'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(default=True, upload_to='profile'),
            preserve_default=False,
        ),
    ]
