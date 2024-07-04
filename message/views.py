from django.shortcuts import render
from django.views.generic import ListView
from .models import Message     #models.py  => Message

# Create your views here.
class MessageList(ListView):
    model = Message

    #規則 : 應用程式 / 資料模型_list.html
    #message / message_list.html

    #資料模型_list