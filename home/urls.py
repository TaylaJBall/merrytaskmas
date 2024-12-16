from . import views
from django.urls import path

# Create your views here.
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]