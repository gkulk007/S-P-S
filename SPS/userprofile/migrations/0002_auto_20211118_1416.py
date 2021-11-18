# Generated by Django 3.2.8 on 2021-11-18 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
