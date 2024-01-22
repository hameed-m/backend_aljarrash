from rest_framework import serializers
from .models import Employee, Client, Project, Comment

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        # fields = []

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        # fields = ["name"]

class ProjectSerializer(serializers.ModelSerializer):
    design_eng_name = serializers.SerializerMethodField()
    structural_eng_name = serializers.SerializerMethodField()
    electrical_eng_name = serializers.SerializerMethodField()
    # client_number = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        # fields = "__all__"
        fields = ["id", "stage","project_name","design_eng","architectural_status","structural_status","plumbing_status","electrical_status","client_id","sketch_approval_date","columns_approval_date","typeof_follow_up","investor_affiliation","project_receipt_date","project_type","land_number","land_area","project_location","project_number","sketch_design_progress_status","structural_eng","structural_design_start_date","structural_review","structural_delivery_date","electrical_eng","electrical_design_start_date","electrical_delivery_date","architectural_drawing_start_date","architectural_delivery_date","plumbing_design_start_date","plan_delivery_date","modification_price","created_at","moved_at","deed","identity","land_survey","soil_test","client_form","old_license","civil_defense", "water_authority", "design_eng_name", "structural_eng_name", "electrical_eng_name", "client_number"]

    def get_design_eng_name(self, obj):
        if(obj.design_eng == None):
            return None
        return obj.design_eng.first_name
    
    def get_structural_eng_name(self, obj):
        if(obj.structural_eng == None):
            return None
        return obj.structural_eng.first_name
    
    def get_electrical_eng_name(self, obj):
        if(obj.electrical_eng == None):
            return None
        return obj.electrical_eng.first_name
    
    # def get_client_number(self, obj):
    #     if(obj.client_id == None):
    #         return None
    #     return obj.client_id.phone_number


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        # fields = []