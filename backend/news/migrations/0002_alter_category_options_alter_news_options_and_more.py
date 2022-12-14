# Generated by Django 4.1.1 on 2022-09-20 06:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='body',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default=None, upload_to='uploads/news/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=None, upload_to='uploads/avatar/%Y/%m'),
        ),
    ]
