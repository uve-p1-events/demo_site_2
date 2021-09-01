from django.db import models



# This class is for the resource model in the eventlobby
class Resource(models.Model):
    eventposter = models.ImageField(upload_to='eventknowledgecentre/static/imgs/', blank=True)
    eventname = models.CharField(max_length=100, null=True)
    datetimestart = models.DateTimeField()
    duration = models.IntegerField()
    downloadviewlink = models.CharField(max_length=500, null=True )
