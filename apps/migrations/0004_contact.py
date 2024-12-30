# Generated by Django 5.0.4 on 2024-05-03 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
