# Generated by Django 3.1.7 on 2021-08-27 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210827_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='available_copies',
        ),
        migrations.RemoveField(
            model_name='book',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='book',
            name='total_copies',
        ),
        migrations.RemoveField(
            model_name='book',
            name='type1',
        ),
        migrations.DeleteModel(
            name='Borrower',
        ),
    ]
