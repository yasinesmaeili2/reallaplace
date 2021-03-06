# Generated by Django 4.0.3 on 2022-04-08 08:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_ipadress_post_hits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hits',
            field=models.ManyToManyField(blank=True, null=True, related_query_name='hits', to='main.ipadress'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
