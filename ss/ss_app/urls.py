from django.urls import path
from .import views

urlpatterns = [
    path('login_page', views.login_page, name='login_page'),  # Login_page
    path('home_page', views.home_view, name='home_page'),
    path('registration_page', views.registration_page, name='registration_page'),  # Registration_page
]