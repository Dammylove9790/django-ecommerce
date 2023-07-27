from django.urls import path
from . import views

urlpatterns = [
    
    ####### Product URLs
    path('', views.dashboard, name='dashboard'),
    path('<str:pk>', views.dashboard, name='dashboard_order_delete'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    ####### User URLs
    path('users/dashboard/<str:pk>', views.user_dashboard, name='user_dashboard'),
    path('users/login/', views.user_login, name='user_login'),
    path('users/register/', views.user_register, name='user_register'),
    path('users/all_users/', views.all_user, name='all_users'),
    path('logout/', views.user_logout, name='logout'),

    ####### Products URLs
    path('products/', views.products, name='products'),
    path('products/productDetails/<str:pk>', views.product_details, name='productDetails'),

    ####### Orders URLs
    path('products/checkout/', views.checkout, name='checkout'),
    path('products/create_order/', views.create_order, name='create_order'),
    path('products/all_orders/', views.all_orders, name='all_orders'),
    path('products/create_order/<str:pk>?update=True', views.update_order, name='update_order'),
    path('products/delete_order/<str:pk>?delete=True', views.delete_order, name='delete_order'),

    # ####### Admin URLs
    # path('admin/dashboard', admin_dashboard, name='admin_dashboard'),
    # path('admin/login', admin_login, name='admin_login'),
    # path('admin/register/', admin_register, name='admin_register'),
]
