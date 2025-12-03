from django.urls import path  # Import Django's path function to define routes
from . import views  # Import views from the current app

# Define URL patterns for this app
urlpatterns = [
    # Root URL ('/') will show the main page with the download form
    path('', views.download_page, name='download_page'),  

    # URL '/download/' will handle the form submission (POST request)
    path('download/', views.download, name='download_video'),  
]
