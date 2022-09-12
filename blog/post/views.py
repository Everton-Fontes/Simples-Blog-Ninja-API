from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


async def index(request: HttpRequest):
    return HttpResponse('Hello Worlds')


async def detail(request: HttpRequest, pk: int):
    return HttpResponse(f'pk = {pk}')
