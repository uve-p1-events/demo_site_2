from django.shortcuts import render

from history.mixins import ObjectViewMixin
from django.views import View
from login.models import User, Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# from .models import OneOnOneRoom
# from .models import Message

# for ajax-chat
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect                            # for loading http response
from django.contrib import  messages                                                                        # for informing the form about some error or giving message
from django.contrib.auth.models import (User, auth)                                                         # for verifying users
from django.shortcuts import render, redirect                                                               # for rendering the template http file
from django.urls import reverse
# from .models import Messages, UserStatus, Groups
from .models import Messages, UserStatus
from django.http import JsonResponse
import datetime, json

# Create your views here.

@method_decorator(login_required, name='dispatch')
class help_desk(ObjectViewMixin, View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



    def get(self, request):
        _owner = request.user.username
        users = []
        if request.user.profile.is_sitehelper:
            users = UserStatus.objects.filter(reader=_owner)
        else:
            users = User.objects.filter(profile__is_sitehelper=True)

        # print(request.user.profile.is_sitehelper)
        # print("users", users)

        # return render(request, "eventhelpdesk/chat.html", context={"allUsers": set(users), "is_sitehelper_flag":request.user.profile.is_sitehelper, "sessionOwner": _owner})
        return render(request, "eventhelpdesk/chat.html", context={"allUsers": set(users), "is_sitehelper_flag":request.user.profile.is_sitehelper, "sessionOwner": _owner})

        # # print(request.user.profile.is_helper)
        # if not request.user.profile.is_sitehelper:
        #     helper_profiles = []
        #     for user in User.objects.filter(profile__is_sitehelper=True):
        #         helper_profiles.append(
        #             [user.first_name, user.last_name,user.email, user.username])
        #         if not (OneOnOneRoom.objects.filter(room_name__contains="help").filter(room_name__contains=request.user.username).filter(room_name__contains=user.username).exists()):
        #                 OneOnOneRoom.objects.create(room_name="help"+"."+user.username+"_"+request.user.username)
                
        #     return render(request,
        #                   "eventhelpdesk/help.html",
        #                   {
        #                       'helper_profiles': helper_profiles,
        #                   },
        #                   )
        # else:
        #     users_visited_profiles = []
        #     for room in OneOnOneRoom.objects.filter(room_name__contains="help.").filter(room_name__contains=request.user.username):
        #         # print("\n\n\n\n\n")
        #         user = User.objects.filter(username = room.room_name.split("_")[1])[0]
        #         # print(len(Message.objects.filter(room__contains=user.username).filter(room__contains=request.user.username).filter(room__contains="help").filter(status="unread")))
        #         users_visited_profiles.append(
        #             [user.first_name, user.last_name, user.email, user.username, len(Message.objects.filter(room__contains=user.username).filter(room__contains=request.user.username).filter(room__contains="help").filter(status="unread"))])
        #     return render(request,
        #                   "eventhelpdesk/help.html",
        #                   {"users_visited_profiles": users_visited_profiles,
        #                    })


# @login_required(login_url="/")
# def chat(request):
#     _owner = request.user.username
#     users = []
#     if request.user.profile.is_sitehelper:
#         users = UserStatus.objects.filter(reader=_owner)
#     else:
#         users = User.objects.filter(profile__is_sitehelper=True)

#     # print(request.user.profile.is_sitehelper)
#     # print("users", users)

#     return render(request, "eventhelpdesk/chat.html", context={"allUsers": set(users), "is_sitehelper_flag":request.user.profile.is_sitehelper, "sessionOwner": _owner})



@login_required(login_url="/")
def getChatUserInfo(request):
    _owner = request.user.username
    _user = request.POST.get('user', None)

    if _user != _owner:
        # print("recipt user is ", _user)
        if User.objects.filter(username=_user).exists():
            if UserStatus.objects.filter(owner=_owner, reader=_user, onGroup=False).exists():
                user_status = UserStatus.objects.filter(owner=_owner, reader=_user, onGroup=False)[0]
                user_status.reader = _user
                user_status.onGroup = False
                user_status.groupId = None
                user_status.timestamp = datetime.datetime.now()
                user_status.save()
            else:
                user_status = UserStatus.objects.create(owner=_owner, reader=_user, onGroup=False, groupId=None, timestamp=datetime.datetime.now())
                user_status.save()

            return JsonResponse({"sessionOwner": _owner, "reader": _user, "onGroup": False, "groupId": 123, "currentTimestamp": user_status.timestamp, "is_sitehelperflag": request.user.profile.is_sitehelper})

        else:
            return JsonResponse({"message": "please provide a valid username to chat with"}, safe=False)
    else:
        return JsonResponse({"message": "you can not talk to yourself, please mention name of ther user to chat with"}, safe=False)



@login_required(login_url="/")
def log_message(request):
    # print("request value is ==>> ", request)
    if request.method == "POST":
        _owner = request.user.username
        _msg = request.POST.get("msg", "")
        _reader = request.POST.get("recipient", None)
        _group_flag = True if request.POST.get("groupFlag", False) == str("true") else False
        _group_id = None if (request.POST.get("group_id", None) == str('None') or request.POST.get("group_id", None) == str('')) else request.POST.get("group_id", None)

        # print("==========================================================", type(request.POST.get("groupFlag", False)))
        # print(_group_flag)
        # for chcking the status of groups as protected or open.
        # if group prtection flag is true then by default the message send in group will have approved status as false since the moderator has to approve the message status to be displayed on the group.

        # print("here owner is {} and message is {} {} {} {} {} ".format(_owner, _msg, _reader, _group_flag, _group_id))
        message = Messages.objects.create(text=_msg, owner=_owner, timestamp=datetime.datetime.now(), recipient=_reader, isGroup=_group_flag, groupId=_group_id, approval_status=True)
        
        try:
            message.save()
            # print("message saved successfully")
        except :
            # print("something happened and message is not saved to database")
            pass
        
        return JsonResponse({"message":"Message sent Successfully"}, safe=False)

    else:
        return JsonResponse({"message":"Please do post request to this link to perform the desire task i.e. to send your message"}, safe=False)


def get_all_chats(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            all_chats = []
            typing_status_users_list = []
            status = request.POST.get("typingStatus", False)
            _owner = request.user.username
            _reader = request.POST.get("recipient", None)
            _group_flag = True if request.POST.get("groupFlag", False) == str("true") else False
            # print("=======>>>>>>>>>>.", request.POST.get("group_id", None))
            # print("=======>>>>>>>>>>.group flag ", request.POST.get("groupFlag", None))
            _group_id = None if (request.POST.get("group_id", None) == str('None') or request.POST.get("group_id", None) == str('')) else request.POST.get("group_id", None)
            _time_stamp = request.POST.get("currentStamp", datetime.datetime.now())

            # print("========>>>>>>>>>>>>here owner is {} and message is {} {} {} {} ".format(_owner, _reader, _group_flag, _group_id, _time_stamp))

            update_typing_status = UserStatus.objects.filter(owner=_owner)[0]
            update_typing_status.typing_status = False if status == str("false") else True
            update_typing_status.reader = _reader
            update_typing_status.onGroup = _group_flag
            update_typing_status.groupId = _group_id
            update_typing_status.timestamp = datetime.datetime.now()
            update_typing_status.save()

            if _group_flag:
                chats = Messages.objects.all().filter(isGroup=True, groupId=_group_id, approval_status=True).order_by('-timestamp')[:20][::-1]
                typing_status = UserStatus.objects.all().filter(onGroup=True, groupId=_group_id, typing_status=True)
                # print("chat is ==============>>>>>>>>", chats)
                for chat in chats:
                    dict_object = chat.get_items_as_dict()
                    all_chats.append(dict_object)

                # for s in typing_status:
                #     typing_obj = s.get_status()
                #     typing_status_users_list.append(typing_obj)

                # print(list(typing_status_users_list))
                return JsonResponse({"chats": all_chats, "group_flag": True}, safe=False)

            else:
                chats = Messages.objects.all().filter(isGroup=False, owner=_owner, recipient=_reader).union(Messages.objects.all().filter(isGroup=False, owner=_reader, recipient=_owner)).order_by('-timestamp')[:20][::-1]
                # print("chat is ==============>>>>>>>>", chats)

                for chat in chats:
                    dict_object = chat.get_items_as_dict()
                    all_chats.append(dict_object)
                # print(list(all_chats))    
            
                try:
                    typing_status = UserStatus.objects.all().filter(onGroup=False, owner=_reader, reader=_owner)[0]
                    return JsonResponse({"chats": all_chats, "typing_status": typing_status.get_typing_status(), "group_flag": False}, safe=False)
                except:
                    # print("Owner with user name {} does not yet started to talk to the guy with name {}".format(_reader, _owner))   
                    return JsonResponse({"chats": all_chats, "typing_status": False, "group_flag": False}, safe=False)

        else:
            return JsonResponse({"message": "sigin first to see the message"}, safe=False)
    
    else:
        return JsonResponse({"message": "Please do request with a valid request type and verified account to get the service"}, safe=False)



def load_previous_messages(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            all_chats = []
            msg_data = json.loads(request.POST.get("dataObject"))
            _owner = request.user.username
            _reader = request.POST.get("recipient", None)
            _group_flag = True if request.POST.get("groupFlag", False) == str("True") else False
            _group_id = None if request.POST.get("group_id", None) == str('None') else request.POST.get("group_id", None)

            if _group_flag:
                chats = Messages.objects.all().filter(isGroup=True, groupId=_group_id, timestamp__lte=msg_data['normal_timestamp'], approval_status=True).order_by('-timestamp')[:20][::-1]
         
                for chat in chats:
                    dict_object = chat.get_items_as_dict()
                    all_chats.append(dict_object)
            
                return JsonResponse({"chats": all_chats, "group_flag": True}, safe=False)

            else:
                chats = Messages.objects.all().filter(isGroup=False, owner=_owner, recipient=_reader, timestamp__lte=msg_data['normal_timestamp']).union(Messages.objects.all().filter(isGroup=False, owner=_reader, recipient=_owner, timestamp__lte=msg_data['normal_timestamp'])).order_by('-timestamp')[:20][::-1]

                for chat in chats:
                    dict_object = chat.get_items_as_dict()
                    all_chats.append(dict_object)

                # print(list(all_chats))
                return JsonResponse({"chats": all_chats, "group_flag": False}, safe=False)

        else:
            return HttpResponse("sigin first to see the message")
    
    else:
        return HttpResponse("Please do a post request with verified account to get the service")
