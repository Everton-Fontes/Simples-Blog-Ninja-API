from django.db import models
from post.models import Post
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    comment_title = models.CharField(max_length=150)
    comment_email = models.EmailField()
    comment = models.TextField()
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateField(auto_now_add=True)
    comment_published = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.comment_title}'
