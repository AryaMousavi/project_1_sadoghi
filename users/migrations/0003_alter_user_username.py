# Generated by Django 4.0.2 on 2022-02-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=70, unique=True),
        ),
    ]
