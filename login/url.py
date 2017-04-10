from django.conf.urls import include,url
from . import views

urlpatterns=[
    #url(r'^$', views.congrats, name='congrats'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<signup_id>[0-9]+)$', views.congrats, name='congrats'),
]
