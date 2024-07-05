from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , DeleteView
from .models import Message     #models.py  => Message

# Create your views here.
class MessageList(ListView):
    model = Message

    #頁面範本檔案名稱 : 應用程式 / 資料模型_list.html  =>  message / message_list.html
    #頁面範本變數名稱 : 資料模型_list => message_list
#預設pk
class MessageRead(DetailView):
    model = Message

    #頁面範本檔案名稱 : 應用程式 / 資料模型_detail.html  =>  message / message_detail.html
    #頁面範本變數名稱 : 資料模型  =>  message

class MessageNew(CreateView):
    model  = Message    #資料模型
    fields = ['user' , 'receipt' , 'subject' , 'content']   #指定顯示
    #fields = '__all__' 全部顯示
    success_url = '/message/'   # 成功新增後要導向的路徑

    #頁面範本檔案名稱 : 應用程式 / 資料模型_form.html  =>  message / message_form.html
    #頁面範本變數名稱 : 資料模型  =>  message