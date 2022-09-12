from django.contrib import admin
from .models import Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_title", 'comment_email',
                    'comment_post', 'comment_date', 'comment_published',)
    list_display_links = ("comment_title", )
    search_fields = ('comment_title', 'comment_date', 'comment_user')
    list_per_page: int = 10
    list_editable = ('comment_published',)


admin.site.register(Comment, CommentAdmin)
