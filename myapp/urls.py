"""
    @author Marlvin Chihota
    Email info@marlvinzw.me
    Created on 18/6/2021
"""

from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import SendEmail

urlpatterns = [
    path("mytask", SendEmail.as_view(), name='register'),
]
