from django.urls import path

from . import views

app_name = 'sanek'
urlpatterns = [
    path('', views.index, name='index'),
    path('store/<int:store_id>/', views.store, name='store'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('stores/', views.storesAll, name='stores'),
    path('products/', views.productsAll, name='products'),

]