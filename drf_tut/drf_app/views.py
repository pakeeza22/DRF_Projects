from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from .serializers import StudentModelSerializer


# ViewSet
# class StudentViewSet(viewsets.ViewSet):
#     def list(self,request):
#         std_obj = Student.objects.all()
#         serializer = StudentModelSerializer(std_obj, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         id = pk
#         if id is not None:
#             std_obj = Student.objects.get(pk=id)
#             serializer = StudentModelSerializer(std_obj)
#             return Response(serializer.data)
#
#         std_obj = Student.objects.all()
#         serializer = StudentModelSerializer(std_obj, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = StudentModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, pk):
#         id = pk
#         std_obj = Student.objects.get(pk=id)
#         serializer = StudentModelSerializer(std_obj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Updated'})
#         return Response(serializer.errors)
#
#     def partial_updated(self, request, pk):
#         id = pk
#         std_obj = Student.objects.get(pk=id)
#         serializer = StudentModelSerializer(std_obj, partial=True, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Partial Updated'})
#         return Response(serializer.errors)
#
#
#     def destroy(self, request,pk=None):
#         id = pk
#         std_obj = Student.objects.get(pk=id)
#         std_obj.delete()
#         return Response({'msg': 'Deleted'})


# Model ViewSet
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentROViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
