from django.db import models
from django.contrib import admin

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    weight = models.IntegerField()

class StudentAdmin(admin.ModelAdmin):
    list_filter = ['weight']
    def birthday(self, obj):
        if obj.date_of_birth is not None:
            return obj.date_of_birth.strftime('%d.%m.%Y')
    list_display = ['name', 'birthday', 'weight']
    list_per_page = 10

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} teaches {self.subject}'


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']

class Subject(models.Model):
    name = models.CharField(max_length=100)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']

