# Generated by Django 4.2.5 on 2023-10-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rno', models.IntegerField()),
                ('per', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Python'), (2, 'Data Science'), (3, 'Data Analyst'), (4, 'JAVA')], verbose_name='Blog Category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='detail',
            field=models.CharField(max_length=1000, verbose_name='Blog Details'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Blog Title'),
        ),
    ]