from .models import Employee, Client, Project, Comment
from .serializers import EmployeeSerializer, ClientSerializer, ProjectSerializer, CommentSerializer

from rest_framework.viewsets import ModelViewSet

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

class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



# @api_view()
# def api_employees(request):
#     employees = Employee.objects.all()
#     serializer = EmployeeSerializer(employees, many=True)
#     return Response(serializer.data)

# @api_view()
# def api_employee(request, pk):
#     employee = get_object_or_404(Employee, id = pk)
#     serializer = EmployeeSerializer(employee)
#     return Response(serializer.data)

# @api_view()
# def api_clients(request):
#     clients = Client.objects.all()
#     serializer = ClientSerializer(clients, many=True)
#     return Response(serializer.data)

# @api_view()
# def api_client(request, pk):
#     client = get_object_or_404(Client, id = pk)
#     serializer = ClientSerializer(client)
#     return Response(serializer.data)

# @api_view()
# def api_stages(request):
#     stages = Stage.objects.all()
#     serializer = StageSerializer(stages, many=True)
#     return Response(serializer.data)

# @api_view()
# def api_stage(request, pk):
#     stage = get_object_or_404(Stage, id = pk)
#     serializer = StageSerializer(stage)
#     return Response(serializer.data)

# @api_view(['GET', 'POST'])
# def api_projects(request):
#     if request.method == 'GET':
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = ProjectSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def api_project(request, pk):
#     project = get_object_or_404(Project, id = pk)
#     if request.method == 'GET':
#         serializer = ProjectSerializer(project)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         serializer = ProjectSerializer(project, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     if request.method == 'DELETE':
#         project.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# @api_view(['GET', 'POST'])
# def api_comments(request):
#     if request.method == 'GET':
#         comments = Comment.objects.all()
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = CommentSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def api_comment(request, pk):
#     comment = get_object_or_404(Comment, id = pk)
#     if request.method == 'GET':
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         serializer = CommentSerializer(comment, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     if request.method == 'DELETE':
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)