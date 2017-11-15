from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^post/list.html$', views.list, name='list'),#ищет представление в views.py
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    
    
]