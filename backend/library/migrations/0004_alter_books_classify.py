# Generated by Django 4.1.1 on 2022-09-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_books_classify_alter_books_source_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='classify',
            field=models.IntegerField(choices=[(0, 'Tự nhiên'), (1, 'Xã hội')], default=1),
        ),
    ]
