from .models import Employee, Client, Project, Comment, TableView
from .serializers import EmployeeSerializer, ClientSerializer, ProjectSerializer, CommentSerializer, TableViewSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
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
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['stage']

class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TableViewViewSet(ModelViewSet):
    queryset = TableView.objects.all()
    serializer_class = TableViewSerializer

    filterset_fields = ['employee', 'stage']


# Learn Authentication
class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)