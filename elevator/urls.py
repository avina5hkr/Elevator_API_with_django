from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.create_new_elevator, name='create_new_elevator'),
]