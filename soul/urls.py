from django.urls import path
from . import views

urlpatterns = [
    path('', views.download_page, name='download_page'),  # Homepage with form
    path('download/', views.download, name='download_video'),  # Form POST target
]
