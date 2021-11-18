# Generated by Django 3.2.8 on 2021-11-18 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('phone_no', models.CharField(max_length=15)),
                ('summary', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('education', models.TextField(blank=True, null=True)),
                ('instagram', models.CharField(max_length=300)),
                ('facebook', models.CharField(max_length=300)),
                ('twitter', models.CharField(max_length=300)),
                ('linkedin', models.CharField(max_length=300)),
                ('github', models.CharField(max_length=300)),
                ('website', models.CharField(max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
