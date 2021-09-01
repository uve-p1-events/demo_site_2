from django.shortcuts import render
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from eventexhibition.models import Exibitor
from login.models import User
from history.mixins import ObjectViewMixin
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import hashlib
import hmac
import base64
import time



@method_decorator(login_required, name='dispatch')
class exibit_view(ObjectViewMixin, View):

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
      
        
            return render(request, 'eventexhibition/exibitors.html',)
                         
                          

@login_required()
def uve_view(request):
    return render(request,'eventexhibition/uve.html')

@login_required()
def kartavya_view(request):
    return render(request,'eventexhibition/kartavya.html')

@login_required()
def getMega_view(request):
    return render(request,'eventexhibition/getMega.html')

@login_required()
def herody_view(request):
    return render(request,'eventexhibition/herody.html')

