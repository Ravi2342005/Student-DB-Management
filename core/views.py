from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count
from .models import Student, Course, Mark
from .forms import StudentForm, CourseForm, MarkForm

# Dashboard
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_students'] = Student.objects.count()
        context['total_courses'] = Course.objects.count()
        
        # Calculate overall pass percentage (simple version)
        all_marks = Mark.objects.all()
        pass_count = sum(1 for m in all_marks if m.is_pass)
        total_marks_records = all_marks.count()
        pass_percentage = (pass_count / total_marks_records * 100) if total_marks_records > 0 else 0
        context['pass_percentage'] = round(pass_percentage, 2)
        
        return context

# Student Views
class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'core/student_list.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(first_name__icontains=search_query) | \
                       queryset.filter(last_name__icontains=search_query) | \
                       queryset.filter(enrollment_number__icontains=search_query)
        return queryset.order_by('-created_at')

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'core/student_detail.html'
    context_object_name = 'student'

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'core/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'core/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'core/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')

# Course Views
class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'core/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'core/course_detail.html'
    context_object_name = 'course'

class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'core/course_form.html'
    success_url = reverse_lazy('course-list')

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'core/course_form.html'
    success_url = reverse_lazy('course-list')

class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'core/course_confirm_delete.html'
    success_url = reverse_lazy('course-list')

# Mark Views
class MarkCreateView(LoginRequiredMixin, CreateView):
    model = Mark
    form_class = MarkForm
    template_name = 'core/mark_form.html'
    
    def get_success_url(self):
        return reverse_lazy('student-detail', kwargs={'pk': self.object.student.pk})

class MarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Mark
    form_class = MarkForm
    template_name = 'core/mark_form.html'
    
    def get_success_url(self):
        return reverse_lazy('student-detail', kwargs={'pk': self.object.student.pk})
