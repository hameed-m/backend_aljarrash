from django.urls import path
from .views import EmployeesViewSet, ClientsViewSet, ProjectsViewSet, CommentsViewSet, TableViewViewSet, HelloView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("employees", EmployeesViewSet)
router.register("clients", ClientsViewSet)
router.register("projects", ProjectsViewSet)
router.register("comments", CommentsViewSet)
router.register("table_views", TableViewViewSet)

urlpatterns = router.urls + [
    path("hello/", HelloView.as_view(), name="hello"),
    path("auth/", obtain_auth_token, name='api_token_auth'),
]