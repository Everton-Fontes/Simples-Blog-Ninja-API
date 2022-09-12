from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", 'author', 'date', 'published')
    list_display_links = ("title", )
    search_fields = ('title', 'date',)
    list_per_page: int = 10
    list_editable = ('published',)


admin.site.register(Post, PostAdmin)
