# Generated by Django 4.2.7 on 2024-03-09 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monday', '0005_rename_electrical_eng_name_project_electrical_eng_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('stage', models.CharField(choices=[('1', 'Sketch'), ('2', 'Sketch Review'), ('3', 'Approval Before Columns'), ('4', 'Awaiting Client Approval On Columns'), ('5', 'Implementation Phase'), ('6', 'Project Review In Autocad'), ('7', 'Ready For Printing After Review'), ('8', 'Review And Sign The Review Copy'), ('9', 'Ready To Receive The Review Copy'), ('10', 'Client Received The Review Copy'), ('11', 'Modifying Clients Notes'), ('12', 'Ready For Final Receipt'), ('13', 'Awaiting Completion Of The Plans'), ('14', 'Completed Projects'), ('15', 'Inactive Projects')], max_length=100)),
                ('view', models.BinaryField(blank=True, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]