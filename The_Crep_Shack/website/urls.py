from django.urls import path
from . import views
from .views import home


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('all_products', views.all_products, name='all_products'),
    path('terms/', views.terms, name='terms'),
    path('faq/', views.faq, name='faq'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:title>', views.category, name='category'),
    path('product/<int:product_id>/', views.product_category, name='product_detail'),
]
