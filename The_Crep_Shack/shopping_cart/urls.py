from django.urls import path
from . import views



urlpatterns = [
    path('', views.cart_summary, name="cart_summary"),
    path('add/', views.cart_add, name="cart_add"), # type: ignore
    path('delete/', views.cart_delete, name="cart_delete"), # type: ignore
    path('update/', views.cart_update, name="cart_update"), # type: ignore
]
