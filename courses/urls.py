from django.urls import path

from .views import *

urlpatterns = [
                path("courses/", CourseApiView.as_view()),
                path("course_update/<int:pk>/", CourseDetailView.as_view()),
                path("students/", StudentApiView.as_view()),
                path("student_update/<int:pk>/", StudentDetailView.as_view()),
                path("syllabus/", SyllabusApiView.as_view()),
                path("syllabus_update/<int:pk>/", SyllabusDetailView.as_view())
]