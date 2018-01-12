import markdown
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from bilibiliapp.models import Post, BilibiliApp


def hello(request):
    return render(request, 'bilibiliapp/index.html', context={
        'title': 'bilibiliapp',
        'welcome': '欢迎访问API'
    })


def index(request):
    post_list = Post.objects.all().order_by('-created_time')

    return render(request, 'bilibiliapp/index.html', context={
        'post_list': post_list
    })


def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions={
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    })
    return render(request, 'bilibiliapp/single.html', context={
        'post': post
    })


def pic(request):
    pic_list = list(BilibiliApp.objects.values())
    return JsonResponse(pic_list, safe=False)
