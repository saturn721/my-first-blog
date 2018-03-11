from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'/index.html$', views.message, name='message'), #index
    url(r'/request.html$', views.message, name='message'),


]
