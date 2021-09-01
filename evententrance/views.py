from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def entrance_view(request):
    username = request.user.username
    return render(request,'evententrance/welcome.html', context={"username": username})
