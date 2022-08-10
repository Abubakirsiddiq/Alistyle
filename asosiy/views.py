from django.shortcuts import render, redirect
from django.views import View
from .models import *

class AsosiyView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "page-index-2.html")
        return redirect("login")


class IchkiView(View):
    def get(self, request, pk):
        b=Bolim.objects.get(id=pk)
        i=Ichki.objects.filter(bolim=b)
        return render(request, "page-category.html", {"ichki":i})


class BolimlarView(View):
    def get(self, request):
        b=Bolim.objects.all()
        return render(request, "page-category.html", {"bolimlar":b})


class TanlanganView(View):
    def get(self, request):
        return render(request, "page-profile-wishlist.html")


class SavatView(View):
    def get(self, request):
        return render(request, "page-shopping-cart.html")


class BuyurtmaView(View):
    def get(self, request):
        return render(request, "page-profile-orders.html")

