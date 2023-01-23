# Generated by Django 4.1.5 on 2023-01-22 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=40)),
                ('speciality', models.CharField(max_length=200)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=9)),
                ('education', models.CharField(max_length=300)),
                ('experience', models.TextField()),
                ('portfolio', models.TextField()),
                ('title', models.CharField(max_length=60)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
