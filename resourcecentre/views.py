from django.shortcuts import render
from history.mixins import ObjectViewMixin
from django.views import View
from .models import Resource
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

@method_decorator(login_required, name='dispatch')
class knowledgecentre_view(ObjectViewMixin, View):

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



    def get(self, request):
        #these 5 lists below are for the objects of the resource centre present in the eventlobby 
        eventnameslist =[]
        eventposterlist=[]
        durationlist=[]
        datetimelist=[]
        downloadviewlinklist=[]
        downloadlinklist=[]

        # Putting elements from admin side into the lists
        for resources in Resource.objects.all():
            eventnameslist.append(resources.eventname)
            eventposterlist.append(resources.eventposter)
            durationlist.append(resources.duration)
            datetimelist.append(resources.datetimestart)
            downloadviewlinklist.append(resources.downloadviewlink)
            modurl='https://drive.google.com/uc?id='+resources.downloadviewlink.split("/")[-2]+'&export=download'
            downloadlinklist.append(modurl)

        #zipping the 5lists into one list
        mylist =zip(eventposterlist,eventnameslist,datetimelist,durationlist,downloadviewlinklist, downloadlinklist)
    
        return render(request,'resourcecentre/knowledgecentre.html',{'mylist':mylist})
