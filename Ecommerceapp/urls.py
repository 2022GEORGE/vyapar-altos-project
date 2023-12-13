from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   path('',views.homepage,name='homepage'),
   path('loginpage',views.loginpage,name='loginpage'),
   path('registration',views.registration,name='registration'),
   path('doregistration',views.doregistration,name='doregistration'),
   path('dologin',views.dologin,name='dologin'),
   path('cart',views.cart,name='cart'),
   path('logout',views.logout,name='logout'),
   path('profile',views.profile,name='profile'),
   path('add_to_cart/<int:pk>',views.add_to_cart,name='add_to_cart'),
   path('remove_from_cart/<int:pk>',views.remove_from_cart,name='remove_from_cart'),
   path('add/<int:pk>',views.add,name='add'),
   path('less/<int:pk>',views.less,name='less'),
   path('makepayment',views.makepayment,name='makepayment'),
   path('do_payment',views.do_payment,name='do_payment'),
   path('paymet',views.payment,name='payment'),
   path('view_item/<int:pk>',views.view_item,name='view_item'),
   path('add_to_wish<int:pk>',views.add_to_wish,name='add_to_wish'),
   path('wishlist_page',views.wishlist_page,name='wishlist_page'),
   path('about',views.about,name='about'),
   path('wish_to_cart<int:pk>',views.wish_to_cart,name='wish_to_cart')
]