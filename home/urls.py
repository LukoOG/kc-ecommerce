from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('products/', views.product, name='product'),
    #path('product_detail/', views.product_detail, name='product_detail'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
]
