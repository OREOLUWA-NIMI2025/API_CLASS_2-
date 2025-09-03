"""
URL configuration for PROJECT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import list_students, retreive_student, create_students, update_student, delete_student
from students.views import list_courses, retreive_course, create_courses,update_course, delete_course
urlpatterns = [
    path('admin/', admin.site.urls),
    path('all/', list_students, name="list_students"),
    path('courses/', list_courses, name='list-courses'),
    path('all/<int:id>/', retreive_student, name="retreive_student"),
    path('courses/<int:id>/',retreive_course, name='retreive_course'),
    path('all/<int:id>/update/', update_student, name='update_student'),
    path('courses/<int:id>/update/', update_course, name='update_course'),
    path('create/', create_students, name='create_student'),
    path('create/course/', create_courses, name='create_courses'),
    path('delete/<int:id>/', delete_student, name='delete-student'),
    path('delete/course/<int:id>/', delete_course, name='delete-course')
]
