from django.conf.urls import url
from . import views

urlpatterns = [
    url('apologize', views.apologize, name='apologize'),
    url('', views.index, name='index'),
]
