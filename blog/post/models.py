from django.db import models
from django.contrib.auth.models import User
from category.models import Category
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.TextField()
    excerpt = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        blank=True
    )
    image_title = models.ImageField(
        blank=True,
        null=True,
        upload_to='fotos/%Y/%m/'
    )
    published = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.title}'
