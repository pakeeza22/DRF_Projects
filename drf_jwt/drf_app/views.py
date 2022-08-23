from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Student
from .serializers import StudentModelSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
