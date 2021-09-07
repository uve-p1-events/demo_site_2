from django.shortcuts import render

# from .models import Event, HallLink
from history.mixins import ObjectViewMixin
from django.views import View
import json
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import json
import sys
import hashlib
import hmac
import base64
import time
# from zoomus import ZoomClient
# Create your views here.

ZoomIdList = []
ZoomIdList.append('96463900558')
# eventVideoDict = {
#     '1': "https://www.youtube.com/embed/YmA0pYXPL6w", '2': "https://www.youtube.com/embed/NBsCzN-jfvA", '3': "https://www.youtube.com/embed/tfSS1e3kYeo", '4': "https://www.youtube.com/embed/tfSS1e3kYeo"}
# agenda = Event.objects.all()

def generateSignature(data):
    ts = int(round(time.time() * 1000)) - 30000
    msg = data['apiKey'] + str(data['meetingNumber']) + str(ts) + str(data['role'])
    message = base64.b64encode(bytes(msg, 'utf-8'))
    # message = message.decode("utf-8");    
    secret = bytes(data['apiSecret'], 'utf-8')
    hash = hmac.new(secret, message, hashlib.sha256)
    hash =  base64.b64encode(hash.digest())
    hash = hash.decode("utf-8")
    tmpString = "%s.%s.%s.%s.%s" % (data['apiKey'], str(data['meetingNumber']), str(ts), str(data['role']), hash)
    signature = base64.b64encode(bytes(tmpString, "utf-8"))
    signature = signature.decode("utf-8")
    return signature.rstrip("=")


@method_decorator(login_required, name='dispatch')
class welcome_audi_view(ObjectViewMixin, View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    def get(self,request):
 

        return render(request, 'eventaudi/audi.html',  )

# @method_decorator(login_required, name='dispatch')
# class inside_audi_view(ObjectViewMixin, View):

#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def get(self,request,eventid="",openagenda=True,):
#         enableThirdHall = False
#         backimg = "/static/imgs/H1-H2.jpg"
#         print(request.user.username)
#         if int(request.user.username) in [917030515595,918588031438,917020054769,918145736347,919904243036,918160604810,917568691099,919952188354,917567620199,917490029201,918866296895,918758886665,919359013299,919616518867,919425453807,919711924500,918291235396,919265164190,919080669552,919558636328,917692932452,9109662477960,919833084275,919886666824,919902061734,918866559857,917666620261,919893052521,917411960901,919730073466,7030515595,8588031438,7020054769,8145736347,9904243036,8160604810,75686099,9952188354,7567620199,7490029201,8866296895,8758886665,9359013299,9616518867,9425453807,9711924500,8291235396,9265164190,9080669552,9558636328,7692932452,9662477960,9833084275,9886666824,9902061734,8866559857,7666620261,9893052521,7411960901,9730073466]:
#             enableThirdHall = True
#             backimg = "/static/imgs/H1-H2-H3.jpg"
#         return render(request, 'eventaudi/home_sessions.html',{"enableThirdHall":enableThirdHall,"backimg":backimg})

# @method_decorator(login_required, name='dispatch')
# class audi_view(ObjectViewMixin, View):
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def get(self,request,eventid="",openagenda=True,):
#         print(request.user.profile.is_moderator)
#         print(eventid)
#         if (eventid != ""):
#             openagenda = False
#         if (str(eventid)=="3"):
#             data = {
#                 'apiKey': "Y4KkcpQcRoewrjlE5X4gnA" ,
#                 'apiSecret': "UiI2SyJ1hlhjafkIAd6ZGbCEHOuXU0PWF5iD",
#                 'meetingNumber': 2823269770,
#                 'role': 1
#                     }
#             signature = generateSignature(data)
#             return render(request, 'eventaudi/meeting.html', {'zoomid':ZoomIdList[0], 'meetingid': '2823269770',"sig":signature,"meetingpassword":"1234"})

#         elif (str(eventid)!=""):
#             return render(request, 'eventaudi/audi.html',
#                     {
#                         'videourl': "https://www.youtube.com/embed/"+HallLink.objects.get(id=int(eventid)).linkIdOnly,
#                         'openagenda': openagenda,
#                         'agenda' : agenda,
#                         'eventid': eventid,
#                     })
        
#         return render(request, 'eventaudi/audi.html',
#                 {
#                     'videourl': "https://www.youtube.com/embed/"+HallLink.objects.get(id=1).linkIdOnly,
#                     'openagenda': openagenda,
#                     'agenda' : agenda,
#                 })
