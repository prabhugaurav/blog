# Generated by Django 4.2.5 on 2023-11-05 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_blog_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='uid',
        ),
    ]
