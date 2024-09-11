from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_dashboard/', views.user_view, name='user_dashboard'),
    path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', views.home_view, name='home'),
]