from django.urls import path

from . import views

urlpatterns = [
    path("",views.login_view,name="login_view"),
    # path("",views.upcoming_event,name="upcoming_event"),
    # path("supportDesk/",views.support_event,name="support_event"),
    path("logout/",views.logout_view,name="logout_view"),
    # path("register/",views.register_view,name="register_view"),
    # path("registration/",views.registeration_view,name="registeration_view"),

    # path('<str:room_name>/', views.room, name='room'),
]