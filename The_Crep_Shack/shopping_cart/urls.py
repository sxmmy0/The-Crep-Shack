from django.urls import path
from . import views



urlpatterns = [
    path('', views.shopping_cart_summary, name="shopping_cart_summary"),
    path('add/', views.shopping_cart_add, name="shopping_cart_add"), # type: ignore
#     path('delete/', views.shopping_cart_delete, name="shopping_cart_delete"),
#     path('update/', views.shopping_cart_update, name="shopping_cart_update"),
]
