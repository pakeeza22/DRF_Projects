import io

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from rest_framework.views import APIView
from .serializers import StudentSerializer, StudentModelSerializer
from .models import Student


@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def get(self, request, *args, **kwargs):
        print("get")
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            std_obj = Student.objects.get(id=id)
            serializer = StudentSerializer(std_obj)
            return JsonResponse(serializer.data, safe=False)

        std_obj = Student.objects.all()
        serializer = StudentSerializer(std_obj, many=True)
        # Json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(Json_data, content_type='application/json')
        return JsonResponse(serializer.data, safe=False)

    def post(self,request, *args, **kwargs):
        print("post")
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            return JsonResponse(res, safe=False)

        return JsonResponse(serializer.errors, safe=False)

    def put(self,request,*args,**kwargs):
        print("put")
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        std_obj = Student.objects.get(id=id)
        serializer = StudentSerializer(std_obj, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated!'}
            return JsonResponse(res, safe=False)

        return JsonResponse(serializer.errors, safe=False)

    def delete(self,request, *args, **kwargs):
        print("delete")
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        std_obj = Student.objects.get(id=id)
        std_obj.delete()
        res = {'msg': 'Data Deleted!'}
        return JsonResponse(res, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class StudentModelApi(View):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def get(self, request, *args, **kwargs):
        print("get")
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            std_obj = Student.objects.get(id=id)
            serializer = StudentModelSerializer(std_obj)
            return JsonResponse(serializer.data, safe=False)

        std_obj = Student.objects.all()
        serializer = StudentModelSerializer(std_obj, many=True)
        # Json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(Json_data, content_type='application/json')
        return JsonResponse(serializer.data, safe=False)

    def post(self,request, *args, **kwargs):
        print("post")
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentModelSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            return JsonResponse(res, safe=False)

        return JsonResponse(serializer.errors, safe=False)

    def put(self,request,*args,**kwargs):
        print("put")
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        std_obj = Student.objects.get(id=id)
        serializer = StudentModelSerializer(std_obj, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated!'}
            return JsonResponse(res, safe=False)

        return JsonResponse(serializer.errors, safe=False)

    def delete(self,request, *args, **kwargs):
        print("delete")
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        std_obj = Student.objects.get(id=id)
        std_obj.delete()
        res = {'msg': 'Data Deleted!'}
        return JsonResponse(res, safe=False)



# @csrf_exempt
# def StudentApi(request):
#     if request.method == 'POST':
#         print("post")
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             return JsonResponse(res, safe=False)
#
#         return JsonResponse(serializer.errors, safe=False)
#
#     elif request.method == "GET":
#         print("get")
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id',None)
#         if id is not None:
#             std_obj = Student.objects.get(id=id)
#             serializer = StudentSerializer(std_obj)
#             return JsonResponse(serializer.data, safe=False)
#
#         std_obj = Student.objects.all()
#         serializer = StudentSerializer(std_obj,many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'PUT':
#         print("put")
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id',None)
#         std_obj = Student.objects.get(id=id)
#         serializer = StudentSerializer(std_obj, data=python_data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Updated!'}
#             return JsonResponse(res, safe=False)
#
#         return JsonResponse(serializer.errors, safe=False)
#
#     elif request.method == 'DELETE':
#         print("delete")
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id',None)
#         std_obj = Student.objects.get(id=id)
#         std_obj.delete()
#         res = {'msg': 'Data Deleted!'}
#         return JsonResponse(res, safe=False)
