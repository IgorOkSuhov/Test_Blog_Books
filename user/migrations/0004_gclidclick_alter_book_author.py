# Generated by Django 4.1.1 on 2023-04-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_age_user_second_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='GcLidClick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='Inkognito', max_length=128),
        ),
    ]
