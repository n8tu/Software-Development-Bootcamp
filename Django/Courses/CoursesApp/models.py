from django.db import models

class CourseManager(models.Manager):
    def validate(request,data):
        errors = {}
        if len(data['course_name']) < 5:
            errors['course_name'] = "Course name length must be more than 5 characters"
        return errors

class DescriptionManager(models.Manager):
    def validate(request,data):
        errors = {}
        if len(data['description']) < 15:
            errors['description'] = "Description length must be more than 15 characters"
        return errors

class Description(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DescriptionManager()

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_description = models.OneToOneField(Description,on_delete=models.CASCADE,related_name="course")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
