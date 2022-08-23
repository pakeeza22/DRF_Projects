from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drf_app.urls')),
    path('auth', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('gettoken/', TokenRefreshView.as_view(),name='token_refresh'),
]
