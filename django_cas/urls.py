from django.conf.urls import url

from . import views

app_name = 'django_cas'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]

