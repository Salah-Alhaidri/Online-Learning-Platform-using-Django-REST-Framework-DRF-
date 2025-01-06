# Online Learning Platform - Django REST Framework

This project is an **Online Learning Platform** built using Django and Django REST Framework (DRF). It allows instructors to create and manage courses, modules, and lessons, while students can enroll in courses, complete lessons, and take quizzes.

## Features

- **User Roles**: Differentiates between students and instructors.
- **Course Management**: Instructors can create courses, add modules, and upload lesson content.
- **Enrollment System**: Students can enroll in courses and track their progress.
- **Quizzes and Assessments**: Instructors can create quizzes with questions and answers, and students can submit their responses.
- **Token-Based Authentication**: Uses DRF's token authentication for secure API access.
- **Nested Serializers**: Represents related models (e.g., courses, modules, lessons) in a single API response.
- **Custom Permissions**: Restricts access to certain actions based on user roles (e.g., only instructors can create courses).

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default), can be configured for PostgreSQL/MySQL
- **Authentication**: Token-based authentication
- **Pagination**: Custom pagination for large datasets
- **Filtering and Searching**: Django Filter and DRF's built-in search functionality



### 1. Clone the Repository

# API Endpoints

## Authentication
- **Login**: `POST /api-token-auth/` (Returns a token for authenticated users)
- **Logout**: Not implemented (Tokens are stateless and must be deleted client-side).

## Courses
- **List Courses**: `GET /generic/courses/`
- **Create Course**: `POST /generic/courses/` (Instructors only)
- **Course Details**: `GET /generic/courses/<int:pk>/`
- **Update Course**: `PUT /generic/courses/<int:pk>/` (Instructors only)
- **Delete Course**: `DELETE /generic/courses/<int:pk>/` (Instructors only)

## Enrollments
- **Enroll in a Course**: `POST /enrollments/enroll/` (Students only)
- **List Enrollments**: `GET /enrollments/`

## Quizzes
- **Submit a Quiz**: `POST /quizzes/<int:pk>/submit/` (Students only)
- **List Quizzes**: `GET /quizzes/`

## Modules and Lessons
- **List Modules**: `GET /modules/`
- **List Lessons**: `GET /lessons/`

---
## Installation

```bash
git clone https://github.com/your-username/online-learning-platform.git
cd online-learning-platform
