from django.contrib import admin
from django.urls import path, include

from SkillStream import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Router for viewsets
router = DefaultRouter()
router.register('enrollments', views.ViewsetEnrollment)
router.register('modules', views.ViewsetModule)

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. Function-Based Views
    path('django/jsonresponsenomodel/', views.no_rest_no_model),
    path('django/jsonresponsefrommodel/', views.no_rest_from_model),

    # 2. Class-Based Views
    path('class-based/profiles/', views.ClassBasedProfileList.as_view()),

    # 3. Generic Views
    path('generic/courses/', views.GenericCourseList.as_view()),
    path('generic/courses/<int:pk>/', views.GenericCourseDetail.as_view()),

    # 4. Viewsets
    path('', include(router.urls)),

    # Token Authentication
    path('api-token-auth/', obtain_auth_token),
]