# Generated by Django 4.0.6 on 2024-01-22 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contactenquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsInformations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('message', models.TextField()),
            ],
        ),
    ]
