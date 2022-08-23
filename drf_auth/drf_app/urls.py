from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

app_name = 'drf_app'

router = DefaultRouter()

router.register('student_ro', StudentViewSet, basename='student')

urlpatterns = router.urls
