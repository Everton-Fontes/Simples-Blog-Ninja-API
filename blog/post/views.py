from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.http import HttpRequest, HttpResponse
from .models import Post
# Create your views here.


async def index(request: HttpRequest):
    return HttpResponse('Hello Worlds')


async def detail(request: HttpRequest, pk: int):
    return HttpResponse(f'pk = {pk}')


class PostIndex(ListView):
    model: Post
    template_name: str = 'post/index.html'
    paginate_by: int = 10
    context_object_name = 'posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('-date')


class PostSearch(PostIndex):
    pass


class PostCategory(PostIndex):
    pass


class PostDetail(UpdateView):
    pass
