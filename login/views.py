from django.shortcuts import render
import os
from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


# Create your views here.

import requests
from django.http import JsonResponse

# def send_otp(request,phone_number):
#     response_data = {}
#     if request.method == "POST":
#         user_phone = phone_number
#         url = "http://2factor.in/API/V1/8c8db630-0e51-11eb-9fa5-0200cd936042/SMS/" + user_phone + "/AUTOGEN/OTPSEND"
#         response = requests.request("GET", url)
#         data = response.json()
#         request.session['otp_session_data'] = data['Details']
#         # otp_session_data is stored in session.
#         response_data = {'Message':'Success'}
#     else:
#         response_data = {'Message':'Failed'}
#     return response_data

# def otp_verification(request,otp):
#     response_data = {}
#     if request.method == "POST":
#         user_otp = otp
#         url = "http://2factor.in/API/V1/8c8db630-0e51-11eb-9fa5-0200cd936042/SMS/VERIFY/" + request.session['otp_session_data'] + "/" + user_otp + ""
#         # otp_session_data is fetched from session.
#         response = requests.request("GET", url)		
#         data = response.json()
#         if data['Status'] == "Success":
#             response_data = {'Message':'Success'}
#         else:
#             response_data = {'Message':'Failed'}
#     return response_data


bypass_list = [str(9592215528),str(9727790271)]
for i in bypass_list:
        i= str(i)

def login_view(request):
    form=LoginForm()
    if request.method == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/welcome/")
            else:
                return render(request,"login/login.html",context={"invalid":True,"form":form})
        else:
            return render(request,"login/login.html",context={"invalid":True,"form":form})
    else:
        return render(request,"login/login.html",context={"invalid":False,"form":form})

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request,'login/profile.html', args)



def welcomemailsender(name_of_new_user, email_of_new_user):

    template = render_to_string('login/confirmationmail.html', {'name_of_new_user':name_of_new_user})

    email = EmailMessage(
        'subject for the mail comes here',       
        template, #body for the mail is the template
        settings.EMAIL_HOST_USER,
        [email_of_new_user],

    )

def logout_view(request):
    try:
        logout(request)
        return redirect("/")
    except Exception as e:
        print(e)
        return redirect("/welcome")

def loaderio_verify_view(request):
    return render(request,"login/loaderio-3fefcf4c2a7c122ddb54ef6d5786c380.html")

def upcoming_event(request):
    
    return render(request,'login/upcoming.html')

def support_event(request):
    
    return render(request,'login/support.html')

