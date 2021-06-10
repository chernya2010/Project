from django.urls import path
from .views import base_view_form

urlpatterns = [
    path('', base_view_form, name='base')
]

