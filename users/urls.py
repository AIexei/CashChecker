from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'$', AuthView.as_view(), name='auth'),
    url(r'^login/$', AuthView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register/success$/', register_success, name='reg_success'),
]