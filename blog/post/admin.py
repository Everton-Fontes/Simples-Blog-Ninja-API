from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", 'author', 'date', 'published')
    list_display_links = ("title", )
    search_fields = ('title', 'date',)
    list_per_page: int = 10
    list_editable = ('published',)
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)
