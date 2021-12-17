# Generated by Django 3.2.7 on 2021-10-10 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=15)),
                ('content', models.TextField(default='', max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
