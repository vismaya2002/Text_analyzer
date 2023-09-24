from django.urls import path
from .views import *

urlpatterns = [
    path('',text_analyzer),
]    