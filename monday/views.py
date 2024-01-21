from .models import Employee, Client, Project, Comment
from .serializers import EmployeeSerializer, ClientSerializer, ProjectSerializer, CommentSerializer

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class EmployeesViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ClientsViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectsViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    filter_fields = ['stage']

class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

