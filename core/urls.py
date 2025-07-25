from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Public pages
    path('', views.home, name='home'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),

    # Authentication-protected pages
    path('book/', login_required(views.book_appointment), name='book_appointment'),
    path('success/', views.success, name='success'),
    path('profile/', login_required(views.profile), name='profile'),

    # Authentication URLs
    path('login/', LoginView.as_view(
        template_name='auth/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
]
