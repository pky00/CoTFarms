from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',auth_views.LoginView.as_view(template_name="login/loginPage.html"),name='loginPage'),
    path('logout/',auth_views.LogoutView.as_view(template_name="login/logoutPage.html"),name='logoutPage'),
]