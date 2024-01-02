from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='app1'
from .forms import LoginForm
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='app1/login.html', authentication_form = LoginForm), name='login'),
]
