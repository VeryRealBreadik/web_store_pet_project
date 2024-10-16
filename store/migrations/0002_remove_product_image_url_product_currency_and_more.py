# Generated by Django 5.1.2 on 2024-10-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(default='RUB', max_length=15),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=2047, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
