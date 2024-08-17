from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('password_reset/', views.password_reset, name='password_reset'),
    #path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    #path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
    path('profile/', views.profile, name='profile'),  # New profile URL pattern
]
