from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeList(APIView):

    def get(self, request):
        emp_obj = Employee.objects.all()
        serializer = EmployeeSerializer(emp_obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
