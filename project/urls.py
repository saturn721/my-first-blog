from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'', include('blog.urls')),#перенаправляет все запросы в файл blog/urls.py
    url(r'^message', include('message.urls'))
]
