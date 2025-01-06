from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from .models import Profile, Course, Enrollment, Module, Lesson, Quiz, Question, Answer, Submission, Response
from .serializers import ProfileSerializer, CourseSerializer, EnrollmentSerializer, ModuleSerializer, LessonSerializer, QuizSerializer, QuestionSerializer, AnswerSerializer, SubmissionSerializer, ResponseSerializer
from rest_framework.views import APIView
from .permissions import IsInstructorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class GenericCourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['instructor', 'created_at']
    search_fields = ['title', 'description']
class GenericCourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsInstructorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)
# 1. Function-Based Views
@api_view(['GET'])
def no_rest_no_model(request):
    return Response({'message': 'This is a response without a model or REST framework.'})

@api_view(['GET'])
def no_rest_from_model(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

# 2. Class-Based Views

class ClassBasedProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 3. Generic Views
class GenericCourseList(generics.ListCreateAPIView):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['instructor', 'created_at']
    search_fields = ['title', 'description']
    permission_classes = [IsInstructorOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

    

class GenericCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# 4. Viewsets
class ViewsetEnrollment(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class ViewsetModule(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer