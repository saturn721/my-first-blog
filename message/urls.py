from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', 'message.views.message', name='message'),
    
]

#url(r'^$', 'message.views.contact', name='contact')