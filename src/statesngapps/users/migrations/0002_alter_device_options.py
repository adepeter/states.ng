# Generated by Django 3.2.8 on 2021-10-24 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'get_latest_by': 'date_logged', 'ordering': ['-date_logged']},
        ),
    ]