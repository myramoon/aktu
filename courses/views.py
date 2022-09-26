from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Student, Syllabus


class StudentApiView(APIView):
    def post(self, request):
        request_data = self.request.data
        student = Student.objects.create(**request_data)
        if not student:
            return Response({"message": "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Student created"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        query_params = self.request.query_params

        filter_query = Q()
        if query_params.get("enrollment_number"):
            filter_query.add(Q(enrollment_number__iexact=query_params.get("enrollment_number")), Q.AND)
        if query_params.get("course"):
            filter_query.add(Q(course_id=query_params.get("course")), Q.AND)
        if query_params.get("syllabus"):
            filter_query.add(Q(syllabus_id=query_params.get("syllabus")), Q.AND)

        students = Student.objects.filter(filter_query).values()

        return Response({
            "result": students,
            "message": "Students retrieved"
        }, status=status.HTTP_200_OK
        )


class StudentDetailView(APIView):
    def put(self, request, pk):
        request_data = self.request.data
        student = Student.objects.filter(id=pk)
        if not student:
            return Response({"message": "Student does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        student.update(**request_data)
        return Response({"message": "Student updated"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        student = Student.objects.filter(id=pk)
        if not student:
            return Response({"message": "Student does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        student.delete()
        return Response({
            "message": "Student deleted"
        }, status=status.HTTP_200_OK)


class CourseApiView(APIView):
    def post(self, request):
        request_data = self.request.data
        Course.objects.create(**request_data)
        return Response({"message": "Course created"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        courses = Course.objects.values()
        return Response({
            "result": courses,
            "message": "Courses retrieved"
        }, status=status.HTTP_200_OK
        )


class CourseDetailView(APIView):
    def put(self, request, pk):
        request_data = self.request.data
        course = Course.objects.filter(id=pk)
        if not course:
            return Response({"message": "Course does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        course.update(**request_data)
        return Response({"message": "Course updated"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        course = Course.objects.filter(id=pk)
        if not course:
            return Response({"message": "Course does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        course.delete()
        return Response({
            "message": "Course deleted"
        }, status=status.HTTP_200_OK)


class SyllabusApiView(APIView):
    def post(self, request):
        request_data = self.request.data
        course = Course.objects.filter(id=request_data.get("course_id"))
        if not course:
            return Response({"message": "Course does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        syllabus = Syllabus.objects.create(**request_data)
        if not syllabus:
            return Response({"message": "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Syllabus created"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        syllabus = Syllabus.objects.values()
        return Response({
            "result": syllabus,
            "message": "Syllabus list retrieved"
        }, status=status.HTTP_200_OK
        )


class SyllabusDetailView(APIView):
    def put(self, request, pk):
        request_data = self.request.data
        syllabus = Syllabus.objects.filter(id=pk)
        if not syllabus:
            return Response({"message": "Syllabus does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        syllabus.update(**request_data)
        return Response({"message": "Syllabus updated"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        syllabus = Syllabus.objects.filter(id=pk)
        if not syllabus:
            return Response({"message": "Syllabus does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        syllabus.delete()
        return Response({
            "message": "Syllabus deleted"
        }, status=status.HTTP_200_OK)
