from django.urls import path
from .views import StudentApi, StudentModelApi

app_name = 'quickstart'
urlpatterns = [
    path('std_api/', StudentApi.as_view(), name='student'),
    path('std_model_api/', StudentModelApi.as_view(), name='student'),
]
