# Generated by Django 4.0.2 on 2022-02-11 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='blog_posts/'),
        ),
    ]
