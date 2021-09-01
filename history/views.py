from django.shortcuts import render
from .models import History
from django.views.generic import ListView, TemplateView


# Create your views here.
class HistoryList(ListView):
    def get_queryset(self):
        user_history = History.objects.filter(user=self.request.user)
        return user_history
        



