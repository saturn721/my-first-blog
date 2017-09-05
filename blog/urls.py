from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),#ищет представление в views.py
]