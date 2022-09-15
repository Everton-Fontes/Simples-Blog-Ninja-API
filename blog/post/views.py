import asyncio
from asgiref.sync import sync_to_async
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpRequest, HttpResponse

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.db.models import Q, Case, When, Count
from django.utils.decorators import classonlymethod

from comments.forms import FormComment
from comments.models import Comment
from .models import Post

from typing import Any
# Create your views here.


class PostIndex(ListView):
    model = Post
    template_name: str = 'post/index.html'
    paginate_by: int = 6
    context_object_name = 'posts'

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    def get_queryset(self):
        """Return the last five published questions."""
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(published=True)
        qs = qs.annotate(
            comment_number=Count(
                Case(
                    When(comment__comment_published=True, then=1)
                )
            )
        )
        return qs

    async def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return await sync_to_async(super().get)(request, *args, **kwargs)


class PostSearch(PostIndex):
    template_name: str = 'post/post_search.html'

    def get_queryset(self):
        """Return the last five published questions."""
        search = self.request.GET.get('s')
        qs = super().get_queryset()
        if not search:
            return qs

        qs = qs.filter(
            Q(title__icontains=search) |
            Q(author__first_name__iexact=search) |
            Q(content__icontains=search) |
            Q(excerpt__icontains=search) |
            Q(category__cat_name__iexact=search)
        )
        return qs


class PostCategory(PostIndex):
    template_name: str = 'post/post_category.html'

    def get_queryset(self):
        """Return the last five published questions."""
        category = self.kwargs.get('category', None)

        qs = super().get_queryset()
        if not category:
            return qs

        qs = qs.filter(
            category__cat_name__iexact=category
        )
        return qs


class PostDetail(UpdateView):
    template_name: str = 'post/post_detail.html'
    model = Post
    form_class = FormComment
    context_object_name = 'post'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Comment.objects.filter(
            comment_published=True,
            comment_post=post.id
        )
        context['comments'] = comments

        return context

    def form_valid(self, form) -> HttpResponse:
        post = self.get_object()
        comment = Comment(**form.cleaned_data)

        comment.comment_post = post

        if self.request.user.is_authenticated:
            comment.comment_user = self.request.user

        comment.save()
        messages.success(self.request, "Comentário Enviado!")
        return redirect('post_detail', pk=post.id)

    # @classonlymethod
    # def as_view(cls, **initkwargs):
    #     view = super().as_view(**initkwargs)
    #     view._is_coroutine = asyncio.coroutines._is_coroutine
    #     return view

    # async def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     return await sync_to_async(super().get)(request, *args, **kwargs)
