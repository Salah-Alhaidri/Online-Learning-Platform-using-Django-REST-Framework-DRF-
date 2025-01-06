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

## Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/online-learning-platform.git
cd online-learning-platform
