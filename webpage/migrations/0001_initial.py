# Generated by Django 2.1.4 on 2019-02-14 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='linux_software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linux_software_name', models.CharField(max_length=200)),
                ('linux_software_location', models.FileField(upload_to='linux_software/')),
            ],
        ),
        migrations.CreateModel(
            name='temp_linux_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=200)),
                ('host_ip', models.CharField(max_length=200)),
            ],
        ),
    ]
