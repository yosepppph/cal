from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    #Login pages
    url(r'^login/$',login, {'template_name': 'users/login.html'}, name='login'),
    #logout page
    url(r'^logout/$', views.logout_view, name='logout'),
    #registration page
    url(r'^register/$', views.register, name='register')
    

]
