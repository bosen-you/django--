from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView
from .models import Message     #models.py  => Message
from django.urls import reverse_lazy , reverse
from django.contrib.auth.mixins import LoginRequiredMixin   #檢測是否有登入 , 沒登入 =>

# Create your views here.
class MessageList(ListView):
    model = Message
    ordering = ['-id']   #反向排序 'id' 排序

    #頁面範本檔案名稱 : 應用程式 / 資料模型_list.html  =>  message / message_list.html
    #頁面範本變數名稱 : 資料模型_list => message_list
#預設pk
class MessageRead(DetailView):
    model = Message

    #頁面範本檔案名稱 : 應用程式 / 資料模型_detail.html  =>  message / message_detail.html
    #頁面範本變數名稱 : 資料模型  =>  message

class MessageNew(LoginRequiredMixin , CreateView):
    model  = Message    #資料模型
    fields = ['user' , 'receipt' , 'subject' , 'content']   #指定顯示
    #fields = '__all__' 全部顯示
    success_url = reverse_lazy('msg_list')  # 成功新增後要導向的路徑

    #頁面範本檔案名稱 : 應用程式 / 資料模型_form.html  =>  message / message_form.html
    #頁面範本變數名稱 : 資料模型  =>  message

class MessageDelete(LoginRequiredMixin , DeleteView):
    model = Message
    success_url = '/message/'

    #頁面範本檔案名稱 : 應用程式 / 資料模型_confirm_deldete.html  =>  message / message_confirm_delete.html
    #頁面範本變數名稱 : form , object , 資料型態(小寫)


