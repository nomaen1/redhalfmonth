from django.urls import path

from apps.base.views import *

urlpatterns = [
    path('', index, name='index')
]