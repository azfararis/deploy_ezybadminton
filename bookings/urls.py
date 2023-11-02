from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    path('', views.index, name='index'),
    
    path('login/', views.login_user, name='login_user'),
    path('signup/', views.signup_user, name='signup_user'),
    path('homepage/', views.homepage, name='homepage'),
    path('booking_page/', views.booking_page, name='booking_page'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('receipt/<int:booking_id>/', views.receipt, name='receipt'),
    path('update_booking/', views.update_booking, name='update_booking'),
    path('delete_booking/', views.delete_booking, name='delete_booking'),
    path('create_booking/<str:user_id>/<str:court_id>/', views.create_booking, name='create_booking'),
]
