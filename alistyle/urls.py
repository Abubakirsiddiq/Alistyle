from django.contrib import admin
from django.urls import path
from asosiy.views import *
from userapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AsosiyView.as_view(),name="asosiy"),
    path('ichkibolim', IchkiView.as_view(),name="ichkibolim"),
    path('bolimlar/', BolimlarView.as_view(),name="bolimlar"),
    path('login', LoginView.as_view(),name="login"),
    path('register', RegisterView.as_view(),name="register"),
    path('tanlangan', TanlanganView.as_view(),name="tanlangan"),
    path('savat', SavatView.as_view(),name="savat"),
    path('buyurtma', BuyurtmaView.as_view(),name="buyurtma"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

