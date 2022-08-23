from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from .models import Student
from .serializers import StudentModelSerializer
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
