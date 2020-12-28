from django.shortcuts import render
from friend.models import FriendList
from django.http import HttpResponse
from account.models import Account


def home_screen_view(request, *args, **kwargs):
    return render(request, 'personal/home.html')



