from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^activation/$', AccountActivationView.as_view(), name='activation'),
    url(r'^validation/$', RegisterValidation.as_view(), name='validation'),
]