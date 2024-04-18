
from django.contrib import admin
from django.urls import path
from petapp import views

urlpatterns = [
    path('home',views.home),
    path('index',views.index),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sort),# for sorted value
    path('range',views.range),
    path('pdetails/<pid>',views.pdetails),
    path('login/',views.log_in),
    path('logout/',views.user_logout),
    path('register',views.register),
    path('contact',views.contact),
    path('addtocart/<pid>',views.addtocart),
    path('viewcart',views.viewcart),
    path('about',views.about),
    path('remove/<cid>',views.remove),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('placeorder',views.placeorder),
    path('makepayment',views.makepayment),
    path('service',views.service),
    path('success',views.success)
]

from django.conf.urls.static import static
from pet import settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)