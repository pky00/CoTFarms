from django.urls import path
from . import views
from Manager.views import CowListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(CowListView.as_view()), name='manager-cow-home'),
    path('AddCow/', views.AddCow, name='manager-cow-addcow'),
    path('EditCow/<int:cowID>', views.EditCow, name='manager-cow-editcow'),
    path('Milk/',views.CowMilk,name='manager-cow-milk'),
    path('Milk/<int:deleteID>',views.CowMilkDelete,name='manager-cow-milk-delete'),
]