from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # Dashboard
    path('', views.DashboardView.as_view(), name='dashboard'),
    
    # Students
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('students/new/', views.StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),
    
    # Courses
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('courses/new/', views.CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course-delete'),
    
    # Marks
    path('marks/new/', views.MarkCreateView.as_view(), name='mark-create'),
    path('marks/<int:pk>/edit/', views.MarkUpdateView.as_view(), name='mark-update'),
]
