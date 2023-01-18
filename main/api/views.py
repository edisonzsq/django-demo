from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View 
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from model.models import Employee
from .helpers import GetBody
import json

class EmployeeView(View):
    def get(self, request):
        all_employees = Employee.objects.all()
        return JsonResponse(json.loads(serialize("json", all_employees)), safe=False)

    def post(self, request):
        body = GetBody(request)
        employee = Employee(name=body["name"], job_title=body["job_title"], income=body["income"])
        employee.save()    
        return JsonResponse(json.loads(json.dumps(model_to_dict(employee))), safe=False) 