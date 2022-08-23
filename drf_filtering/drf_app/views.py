from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from .models import Student
from .serializers import StudentModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


# Concrete API Views
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby='ahmad')
    serializer_class = StudentModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['passby']
    # filterset_fields = ['passby']

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentRtUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentRtDestroy(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
