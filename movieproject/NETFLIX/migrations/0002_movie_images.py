# Generated by Django 3.1 on 2022-05-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NETFLIX', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='images',
            field=models.ImageField(default='', upload_to='Photos'),
            preserve_default=False,
        ),
    ]
