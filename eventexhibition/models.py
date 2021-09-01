from django.db import models
from login.models import User
# Create your models here.


# class Message(models.Model):
#     author = models.ForeignKey(User,related_name='author_messages',on_delete=models.CASCADE)
#     room = models.CharField(max_length=100,null=True)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(default='unread', max_length=6)

#     def __str__(self):
#         return self.author.username + "_" + self.content + "_" + self.room

#     def last_10_messages(room):
#         try:
#             return Message.objects.filter(room__exact=room).order_by('-timestamp').all()[:10]
#         except:
#             return Message.objects.filter(room__exact=room).order_by('-timestamp').all()


class Exibitor(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    brochuredownloadlink = models.CharField(max_length=500, null=True)
    


    def __str__(self):
        return self.name

        
