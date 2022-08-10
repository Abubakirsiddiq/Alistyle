from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .models import *


class LoginView(View):
    def get(self,request):
        return render(request,"page-user-login.html")
    def post(self, request):
        l = request.POST.get("l")
        p = request.POST.get("p")
        userlar = authenticate(request, username=l, password=p)
        if userlar is None:
            return redirect("register")
        login(request, userlar)
        return redirect("asosiy")


class RegisterView(View):
    def get(self, request):
        return render(request, "page-user-register.html")

    def post(self, request):
        u = User.objects.create_user(
            username=request.POST.get('u'),
            password=request.POST.get('p')
        )
        a = Account.objects.create(
            ism=request.POST.get('i'),
            email=request.POST.get('e'),
            jins=request.POST.get('jins'),
            shahar=request.POST.get('sh'),
            mamlakat=request.POST.get('m'),
            user=u
        )
        return redirect("login")

