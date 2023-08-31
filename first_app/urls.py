from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path("", views.MyHomeView.as_view(), name="home"),
    path("student_list/", views.StudentListView.as_view(), name="student_list"),
    path("student_detail/<int:pk>", views.StudentDetailView.as_view(), name="student_detail"),
    path('student_create/', views.StudentCreateView.as_view(), name="student_create"),
    path("student_update/<int:pk>", views.StudentUpdateView.as_view(), name ="student_update"),
    path("student_delete/<int:pk>", views.StudentDeleteView.as_view(), name="student_delete"),
    path('teacher_list/', views.TeacherListView.as_view(), name= 'teacher_list'),
    path('teacher_form_create/', views.TeacherCreateView.as_view(), name='teacher_create'),
]