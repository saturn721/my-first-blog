from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'zalipon.html', views.zalipon, name='zalipon'),

    url(r'^$', views.listen, name='listen'),

    url(r'ru/', views.listru, name='listru'),




]
