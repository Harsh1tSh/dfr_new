from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
import openpyxl
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.
# basically responses to our requests

def index(request):
    return HttpResponse("Welcome to my api backend")

# json response example
@api_view(['GET'])
def json_response_view(request):

    # data = {
    #     'message' : 'hello, this is a JSON Response',
    #     'status' : 'success',
    #     'data' : {
    #         'name' : 'Alex',
    #         'major' : 'Physics',
    #         'age' : 167
    #     }
    # }


    # data = {}
    single_student = Student.objects.all().order_by("?").first()
    

    # if single_student:
    #     data['id'] = single_student.id
    #     data['first_name'] = single_student.first_name
    #     data['last_name'] = single_student.last_name
    #     data['age'] = single_student.age
    #     data['major'] = single_student.major

    data = model_to_dict(single_student, 
                         fields=['id', 'first_name','last_name'])

    return Response(data)


# Class based view example
class CBV_Example(APIView):
    def get(self, request):
        data = {
            'message' : 'This is a CBV Get response'
        }
        return Response(data)
    
    def post(self, request):
        data = {
            'message' : 'This is a CBV Post response'
        }
        return Response(data)
    
    def put(self, request):
        data = {
            'message' : 'This is a CBV Put response'
        }
        return Response(data)
    
    def patch(self, request):
        data={
            'message':'This is a CBV Patch response'
        }
        return Response(data)
    
    def delete(self, request):
        data={
            'message':'This is a CBV Delete response'
        }
        return Response(data)


# import data
def import_students_from_excel(request):

    file_path = r"C:\Users\Harshit Sharma\Hi\dfr_new\students_data.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # Get the fields of the Student model
    model_fields = [field.name for field in Student._meta.get_fields() if field.name != "id"]

    # Iterate over rows and create Student objects
    for row in sheet.iter_rows(min_row=2, values_only=True):
        student_data = dict(zip(model_fields, row))
        # print(student_data)
        Student.objects.create(**student_data)

    return HttpResponse("Import completed")