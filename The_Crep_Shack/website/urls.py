from django.urls import path
from . import views
from .views import item_list

app_name = 'website'

urlpatterns = [
    path('', views.home),
    path('', item_list, name='item-list')
]