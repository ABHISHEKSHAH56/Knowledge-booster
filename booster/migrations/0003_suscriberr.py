# Generated by Django 3.0.5 on 2020-07-31 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booster', '0002_delete_suscribe'),
    ]

    operations = [
        migrations.CreateModel(
            name='suscriberr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
    ]
