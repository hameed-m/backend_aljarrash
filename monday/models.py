from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    phone = models.CharField(max_length=13, null=True, blank=True)

class Client(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        if self.name == None:
            return ""
        return self.name

class ProjectTypes(models.TextChoices):
    New = 'new'
    Addition = 'addition'
    Restoration = 'restoration'

class Status(models.TextChoices):
    Working_on_it = 'Working on it'
    Done = 'Done'
    Hold = 'Hold'
    Not_required = "Not required"

class DesignStatus(models.TextChoices):
    Ground = "Ground floor"
    First = "First floor"
    Second = "Second floor"
    Third = "Third floor"
    Annex = "Annex room"
    Facade = "Facade"

class FollowUpTypes(models.TextChoices):
    Paper = "Paper"
    Municipal = "Municipal"

class StructuralReviewStatus(models.TextChoices):
    Working_on_it = 'Working on it'
    Done = 'Done'


class Stages(models.TextChoices):
    Sketch = 1
    Sketch_Review = 2
    Awaiting_Client_Approval = 3
    Execution_Stage = 4
    AutoCAD_Review = 5
    Ready_to_Print = 6
    Validate_Sign_Review_Copy = 7
    Ready_to_Collect = 8
    Client_Received_Copy = 9
    Edit_Client_Notes = 10
    License_Issuance = 11
    Ready_for_Final_Receipt = 12
    Completed_Projects = 13
    Inactive_Projects = 14



class Project(models.Model):
    stage = models.CharField(max_length=100, choices=Stages.choices, null=False, blank=False)
    project_name = models.CharField(max_length=100, null=True, blank=True)
    design_eng = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='designer', null=True, blank=True)
    architectural_status = models.CharField(max_length=100, choices=Status.choices, null=True, blank=True)
    structural_status = models.CharField(max_length=100, choices=Status.choices, null=True, blank=True)
    plumbing_status = models.CharField(max_length=100, choices=Status.choices, null=True, blank=True)
    electrical_status = models.CharField(max_length=100, choices=Status.choices, null=True, blank=True)
    client_number = models.ForeignKey(Client, on_delete=models.SET_NULL, related_name='client', null=True, blank=True)
    sketch_approval_date = models.DateField(null=True, blank=True)
    columns_approval_date = models.DateField(null=True, blank=True)
    typeof_follow_up = models.CharField(max_length=100, choices=FollowUpTypes.choices, null=True, blank=True)
    investor_affiliation = models.BooleanField(null=True, blank=True)
    project_receipt_date = models.DateField(null=True, blank=True)
    project_type = models.CharField(max_length=100, choices=ProjectTypes.choices, null=True, blank=True)
    land_number = models.CharField(max_length=100, null=True, blank=True)
    land_area = models.FloatField(null=True, blank=True)
    project_location = models.CharField(max_length=100, null=True, blank=True)
    project_number = models.IntegerField(null=True, blank=True)
    sketch_design_progress_status = models.CharField(max_length=100, choices=DesignStatus.choices, null=True, blank=True)
    structural_eng = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='structural_engineer', null=True, blank=True)
    structural_design_start_date = models.DateField(null=True, blank=True)
    structural_review = models.CharField(max_length=100, choices=StructuralReviewStatus.choices, null=True, blank=True)
    structural_delivery_date = models.DateField(null=True, blank=True)
    electrical_eng = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='electrical_engineer', null=True, blank=True)
    electrical_design_start_date = models.DateField(null=True, blank=True)
    electrical_delivery_date = models.DateField(null=True, blank=True)
    architectural_drawing_start_date = models.DateField(null=True, blank=True)
    architectural_delivery_date = models.DateField(null=True, blank=True)
    plumbing_design_start_date = models.DateField(null=True, blank=True)
    plan_delivery_date = models.DateField(null=True, blank=True)
    modification_price = models.FloatField(null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)
    moved_at = models.DateField(null=True, blank=True)

    deed = models.FileField(upload_to="static/deeds/", null=True, blank=True)
    identity = models.FileField(upload_to="static/identities/", null=True, blank=True)
    land_survey = models.FileField(upload_to="static/land_surveys/", null=True, blank=True)
    soil_test = models.FileField(upload_to="static/soil_tests/", null=True, blank=True)
    client_form = models.FileField(upload_to="static/client_forms/", null=True, blank=True)
    old_license = models.FileField(upload_to="static/old_licenses/", null=True, blank=True)
    civil_defense = models.FileField(upload_to="static/civil_defenses/", null=True, blank=True)
    water_authority = models.FileField(upload_to="static/water_authorities/", null=True, blank=True)

    def __str__(self):
        if self.project_name == None:
            return ""
        return self.project_name

class Comment(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)
    written_at = models.DateField(null=True, blank=True)
    attachment = models.FileField(upload_to="static/attachments/", null=True, blank=True)
    written_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    written_for = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.title == None:
            return ""
        return self.title
    
class TableView(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    stage = models.CharField(max_length=100, choices=Stages.choices, null=False, blank=False)
    view = models.CharField(max_length=60, null=True, blank=True)

    