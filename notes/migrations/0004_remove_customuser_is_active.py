# Generated by Django 4.1.6 on 2023-02-11 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_customuser_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
    ]