from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employees", views.EmployeesViewSet)
router.register("clients", views.ClientsViewSet)
router.register("projects", views.ProjectsViewSet)
router.register("comments", views.CommentsViewSet)

urlpatterns = router.urls