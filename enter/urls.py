from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.enter, name='enter'),
    url(r'enter.html$', views.enter, name='enter'),

]
