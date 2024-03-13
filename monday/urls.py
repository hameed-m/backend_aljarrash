from django.urls import path
from .views import EmployeesViewSet, ClientsViewSet, ProjectsViewSet, CommentsViewSet, TableViewViewSet, HelloView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employees", EmployeesViewSet)
router.register("clients", ClientsViewSet)
router.register("projects", ProjectsViewSet)
router.register("comments", CommentsViewSet)
router.register("table_views", TableViewViewSet)

urlpatterns = router.urls + [path("hello/", HelloView.as_view(), name="hello")]