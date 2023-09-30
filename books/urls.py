from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_book/', views.create_book, name='create_book'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('section/edit/<int:section_id>/', views.edit_section, name='edit_section'),
]
