from django.contrib import admin
from .models import Employee, Client, Project, Comment

# Register your models here.
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Comment)