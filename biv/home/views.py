import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class Login(View):
    def post(self,request):
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user_pass = authenticate(username=username, password=password)
        if user_pass:
            return True
        return False

class Register(View):
    def get(self,request):
        username = request.GET.get('username','')
        password = request.GET.get('password','')
        user_pass = User.objects.filter(username=username)
        content = {}
        if user_pass.count()>0:
            content['result'] = 1
            content['msg'] = 'User name already exists'
            return JsonResponse(content)
        else:
            user = User.objects.create_user(username=username,password=password)
            user.is_superuser = 0
            user.is_staff = 1
            user.is_active = 1
            user.date_joined = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
            user.save()
            content['result'] = 0
            content['msg'] = 'Register success'
        return JsonResponse(content)