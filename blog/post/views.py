from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


async def index(request: HttpRequest):
    return 'Hello Worlds'
