# Generated by Django 4.2.5 on 2023-11-05 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_remove_blog_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='uid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
