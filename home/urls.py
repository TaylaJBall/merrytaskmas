from . import views
from .views import HomePage 
from django.shortcuts import redirect
from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy

# Create your views here.
urlpatterns = [
    # Root URL: Redirect unauthenticated users to login, authenticated users to index
    path('', lambda request: redirect('/index/') if request.user.is_authenticated else redirect('account_login'), name='home'),
    # Define the index page (for authenticated users)
    path('index/', HomePage.as_view(), name='index'),
    
]