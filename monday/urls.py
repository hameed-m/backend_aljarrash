from django.urls import path
from .views import HelloView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employees", views.EmployeesViewSet)
router.register("clients", views.ClientsViewSet)
router.register("projects", views.ProjectsViewSet)
router.register("comments", views.CommentsViewSet)
router.register("table_views", views.TableViewViewSet)

urlpatterns = router.urls + [path("hello/", HelloView.as_view(), name="hello")]