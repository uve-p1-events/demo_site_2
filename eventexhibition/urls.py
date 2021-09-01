from django.urls import path

from . import views

urlpatterns = [
    path("",views.exibit_view.as_view(),name="exibit_view"),
    path("getMega/",views.getMega_view, name = "getMega_view"),
    path("kartavya/",views.kartavya_view, name = "kartavya_view"),
    path("herody/",views.herody_view, name = "herody_view"),
    path("ultimatevirtualevent/",views.uve_view, name = "uve_view"),
    

    
]
