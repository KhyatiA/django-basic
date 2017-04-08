from django.conf.urls import include,url
from django.contrib import admin


urlpatterns = [
    url(r'^login/', include('login.url')),
    url(r'^admin/', admin.site.urls),

]
