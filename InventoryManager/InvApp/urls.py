from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createProduct/', views.createProduct, name='createProduct'),
    path('createBrand/', views.createBrand, name='createBrand'),
    path('updateProduct/<int:id>/', views.updateProduct, name='updateProduct'),
    path('deleteProduct/<int:id>/', views.deleteProduct, name='deleteProduct'),
]