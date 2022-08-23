from django.urls import path, include
from .views import StudentViewSet, StudentROViewSet
from rest_framework.routers import DefaultRouter

app_name = 'drf_app'

router = DefaultRouter()

router.register('student_ro', StudentROViewSet, basename='student')

urlpatterns = router.urls
