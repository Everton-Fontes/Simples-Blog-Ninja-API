# Generated by Django 4.1.1 on 2022-09-12 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('excerpt', models.TextField()),
                ('image_title', models.ImageField(blank=True, null=True, upload_to='fotos/%Y/%m/')),
                ('published', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='category.category')),
            ],
        ),
    ]
