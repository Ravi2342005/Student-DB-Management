# Student Management System

A complete Student Management System web application built with Python and Django. This system allows administrators to manage students, courses, enrollments, and marks efficiently.

## Features

- **Authentication**: Secure login/logout system for administrators.
- **Dashboard**: High-level overview of total students, courses, and overall performance.
- **Student Module**: Complete CRUD functionality to register, view, edit, and delete student records. Includes directory search and pagination.
- **Course Module**: Manage course information and enroll multiple students into courses.
- **Marks Module**: Assign and update marks for students in enrolled courses. Automatically calculates percentage and Pass/Fail status (40% passing criteria).

## Technology Stack

- **Backend**: Python 3.13, Django 6
- **Frontend**: HTML5, Vanilla JavaScript, Bootstrap 5 (CSS framework)
- **Database**: SQLite (default Django database)

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Git (optional)

### Installation Steps

1. **Clone or Download the Repository**
   Navigate to the directory where you want to set up the project.

2. **Create a Virtual Environment**
   It's recommended to create a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser (Admin)**
   To access the application, you need to create an administrator account:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set your username, email, and password.

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   Open your web browser and navigate to `http://127.0.0.1:8000/`. Log in using the superuser credentials you created.

## Project Structure
- `student_management/` - Core Django project configuration.
- `core/` - The main application containing Models, Views, Forms, and URLs.
- `templates/core/` - HTML files built with Bootstrap 5.
- `static/core/` - Custom CSS and JS files.
