# Generated by Django 2.2.6 on 2019-12-22 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xfzauth', '0003_auto_20191211_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_avater',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_desc',
            field=models.CharField(default='无', max_length=32),
            preserve_default=False,
        ),
    ]