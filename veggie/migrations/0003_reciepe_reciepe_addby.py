# Generated by Django 5.0 on 2023-12-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggie', '0002_reciepe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciepe',
            name='reciepe_addby',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
