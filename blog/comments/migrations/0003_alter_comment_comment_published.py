# Generated by Django 4.1.1 on 2022-09-14 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comment_comment_alter_comment_comment_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_published',
            field=models.BooleanField(default=False),
        ),
    ]
