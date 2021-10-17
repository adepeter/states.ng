# Generated by Django 3.2.8 on 2021-10-17 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0008_localgovernmentarea_secretariat'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('lga', models.ForeignKey(help_text='LGA district falls under', on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='states.localgovernmentarea')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
