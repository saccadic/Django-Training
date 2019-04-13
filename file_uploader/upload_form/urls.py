from django.conf.urls import url
from .views import form, complete

urlpatterns = [
    url(r'^$', form, name = 'form'),
    url(r'^complete/', complete, name = 'complete'),
]