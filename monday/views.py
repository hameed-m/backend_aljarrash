from .models import Employee, Client, Project, Comment, TableView
from .serializers import EmployeeSerializer, ClientSerializer, ProjectSerializer, CommentSerializer, TableViewSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class EmployeesViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ClientsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['stage']

class CommentsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TableViewViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = TableView.objects.all()
    serializer_class = TableViewSerializer

    filterset_fields = ['employee', 'stage']


# Learn Authentication
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)