from django.db import models
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from .signals import object_viewed_signal
from login.models import User
from datetime import datetime

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed_on       = models.DateTimeField(default= datetime.now)
    url = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return str(self.user)+" __ "+str(self.url)+" __ "+str(self.viewed_on)

    class Meta:
        verbose_name_plural ="Histories"

def object_viewed_reciver( request, *args, **kwargs):
    new_history = History.objects.create(
        user = request.user,
        url = request.get_full_path()
    )

    # author_user = request.user
    # calculatepoints(History.objects.filter(user = author_user))
    # user = User.objects.filter(username= request.user)[0]
    # user.profile.leaderboard_points = calculatepoints(History.objects.filter(user = author_user))
    # user.save() 
object_viewed_signal.connect(object_viewed_reciver)
