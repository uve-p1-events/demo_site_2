from django.urls import path

from . import views

urlpatterns = [
    path("",views.knowledgecentre_view.as_view(),name="knowledgecentre_view"),
]
