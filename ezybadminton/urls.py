from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ezybadminton', include('bookings.urls')),  # Include your app's urls.py here
    # Add more paths as needed
]
