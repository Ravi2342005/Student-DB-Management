from django import forms
from .models import Student, Course, Mark

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'enrollment_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'enrollment_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description', 'students']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'students': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['student', 'course', 'marks_obtained', 'total_marks']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'marks_obtained': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'total_marks': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
