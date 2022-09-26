from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)


class Syllabus(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Student(models.Model):
    enrollment_number = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE)
