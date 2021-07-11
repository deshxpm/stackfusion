from django.urls import path
from sample import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('saveddata/', views.saveddata, name='checkdata'),
]
