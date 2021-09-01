from django.urls import path

from . import views

urlpatterns = [
    path("",views.welcome_audi_view.as_view(),name="audi_view"),
]