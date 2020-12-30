from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='manager-cow-home'),
    path('AddCow/', views.AddCow, name='manager-cow-addcow'),
    path('EditCow/<int:cowID>', views.EditCow, name='manager-cow-editcow'),
]