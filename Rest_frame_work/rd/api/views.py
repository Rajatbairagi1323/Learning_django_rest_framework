from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,  JsonResponse
# Create your views here.

def Student_details(request,pk):
    stu = Student.objects.get(id=pk)
    print(stu)
    serializer = StudentSerializers(stu)
    print(serializer)
    print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

# All Student data 

def Student_list(request):
    stu = Student.objects.all()
    print(stu)
    serializer = StudentSerializers(stu,many = True)
    print(serializer)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')