from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'en/', views.listen, name='listen'),#ищет представление в views.py
    url(r'ru/', views.listru, name='listru'),
    url(r'', include('enter.urls')),



]
