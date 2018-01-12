from django.urls import path
from django.conf.urls import url
from bilibiliapp import views

app_name = 'blog'
urlpatterns = [
    path('index', views.index, name='index'),
    url(r'^$', views.index, name='index2'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.details, name='details'),
    path('pic', views.pic, name='pic')
]
