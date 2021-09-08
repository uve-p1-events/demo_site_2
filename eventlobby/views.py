from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

import os
from history.mixins import ObjectViewMixin
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# from eventaudi.models import Event

@method_decorator(login_required, name='dispatch')
class home_view(ObjectViewMixin, View):

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        return render( request,'eventlobby/home.html', {"room_name" : "lobby"} )


# @login_required()
def profile_view(request):
    return render(request,'login/profile.html')

def logout_view(request):
    try:
        logout(request)
        return redirect("/")
    except:
        return render(request,'eventlobby/home.html',{'lobbybg':os.listdir("eventlobby/static/imgs/")[0]})
