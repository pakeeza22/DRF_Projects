from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .custompermissions import MyPermission

from .models import Student
from .serializers import StudentModelSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


# class StudentViewSet2(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]   # give permission to any user


# class StudentViewSet2(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAdminUser]   # give permission to only admin
