from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from .models import Student
from .serializers import StudentModelSerializer

# Create your views here.
from rest_framework.decorators import api_view


## Function Based API View
# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def student_api(request):
#     if request.method == 'GET':
#         id = request.data.get(id)
#         if id is not None:
#             std_obj = Student.objects.get('id')
#             serializer = StudentModelSerializer(std_obj)
#             return Response(serializer.data)
#
#         std_obj = Student.objects.all()
#         serializer = StudentModelSerializer(std_obj, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = StudentModelSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'PUT':
#         id = request.data.get(id)
#         std_obj = Student.objects.get(pk=id)
#         serializer = StudentModelSerializer(std_obj, partial=True, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Updated'})
#         return Response(serializer.errors)
#
#     elif request.method == 'DELETE':
#         id = request.data.get(id)
#         std_obj = Student.objects.get(pk=id)
#         std_obj.delete()
#         return Response({'msg': 'Deleted'})


## Class Based API View
# class StudentApi(APIView):
#     def get(self,request, pk=None, format=None):
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
#     def post(self, request):
#         serializer = StudentModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk, format=None):
#         id = pk
#         std_obj = Student.objects.get(pk=id)
#         serializer = StudentModelSerializer(std_obj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Updated'})
#         return Response(serializer.errors)
#
#     def patch(self, request, pk, format=None):
#         id = pk
#         std_obj = Student.objects.get(pk=id)
#         serializer = StudentModelSerializer(std_obj, partial=True, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Updated'})
#         return Response(serializer.errors)
#
#
#     def delete(self, request,pk=None, format=None):
#         id = pk
#         std_obj = Student.objects.get(pk=id)
#         std_obj.delete()
#         return Response({'msg': 'Deleted'})

# ## Generic Views
# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#
#     def get(self,request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#
#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#
#     def get(self,request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#
# class StudentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#
#     def put(self,request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#
# class StudentDestroy(GenericAPIView, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#
#     def delete(self,request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


## Concrete API Views
# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#
#
# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#
#
# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#
#
# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer
#
#
# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer


class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


# class StudentRtUpdate(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer


# class StudentRtDestroy(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerializer


class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
