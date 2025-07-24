from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('success/', views.success, name='success'),
]