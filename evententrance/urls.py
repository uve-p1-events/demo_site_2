from django.urls import path

from . import views

urlpatterns = [
    path("",views.entrance_view,name="entrance_view"),

]