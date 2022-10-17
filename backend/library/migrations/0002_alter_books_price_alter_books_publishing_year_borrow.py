# Generated by Django 4.1.1 on 2022-09-24 11:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='publishing_year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2022)]),
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.books')),
                ('borrower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
