from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Student, Course, Mark

class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            date_of_birth="2000-01-01",
            enrollment_number="STU001"
        )
        
    def test_student_str(self):
        self.assertEqual(str(self.student), "Test User (STU001)")

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name="Test Course",
            code="CS101"
        )
        
    def test_course_str(self):
        self.assertEqual(str(self.course), "CS101 - Test Course")

class MarkModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            date_of_birth="2000-01-01",
            enrollment_number="STU002"
        )
        self.course = Course.objects.create(
            name="Test Course 2",
            code="CS102"
        )
        # Testing Pass
        self.mark_pass = Mark.objects.create(
            student=self.student,
            course=self.course,
            marks_obtained=50,
            total_marks=100
        )
        
    def test_percentage(self):
        self.assertEqual(self.mark_pass.percentage, 50.0)
        
    def test_is_pass(self):
        self.assertTrue(self.mark_pass.is_pass)

class MarkModelFailTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="Test2",
            last_name="User2",
            email="test2@example.com",
            date_of_birth="2000-01-01",
            enrollment_number="STU003"
        )
        self.course = Course.objects.create(
            name="Test Course 3",
            code="CS103"
        )
        # Testing Fail
        self.mark_fail = Mark.objects.create(
            student=self.student,
            course=self.course,
            marks_obtained=30,
            total_marks=100
        )
        
    def test_percentage(self):
        self.assertEqual(self.mark_fail.percentage, 30.0)
        
    def test_is_pass(self):
        self.assertFalse(self.mark_fail.is_pass)


class ViewAccessTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        
    def test_dashboard_unauthenticated(self):
        response = self.client.get(reverse('dashboard'))
        self.assertIn(response.status_code, [302, 403])
        
    def test_dashboard_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
