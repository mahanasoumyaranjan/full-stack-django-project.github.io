# Generated by Django 4.0.6 on 2022-07-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('feed', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
