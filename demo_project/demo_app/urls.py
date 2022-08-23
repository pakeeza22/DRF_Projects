from django.urls import path
from .views import EmployeeList
from django.contrib.auth.views import LogoutView

app_name = 'demo_app'
urlpatterns = [
    path('', EmployeeList.as_view(), name='employees'),
]
