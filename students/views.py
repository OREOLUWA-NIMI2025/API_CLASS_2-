from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from .serializers import StudentSerializer, CourseSerializer
from .models import  Student, Course
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def list_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def list_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def retreive_student(request, id):
    student = Student.objects.get(id=id)
    # student = get_object_or_404(student, id=id)
    serializer = StudentSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def retreive_course(request, id):
    course = Course.objects.get(id=id)
    serializer = CourseSerializer(course)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_students(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])   
def create_courses(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["PUT"])
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    serializer = StudentSerializer(student , data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])  
def update_course(request, id):
    course = get_object_or_404(Course, id=id)
    serializer = CourseSerializer(course, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_student(request, id):
    student=get_object_or_404(Student, id=id)
    student.delete()
    return Response("student-delete-successfully", status=status.HTTP_200_OK)

@api_view(["DELETE"])
def delete_course(request, id):
    course=get_object_or_404(Course, id=id)
    course.delete()
    return Response("Course-remove-successfully", status=status.HTTP_200_OK)