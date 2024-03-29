# Generated by Django 4.2.7 on 2024-01-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monday', '0004_project_civil_defense_project_client_form_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='electrical_eng_name',
            new_name='electrical_eng',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='structural_eng_name',
            new_name='structural_eng',
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='moved_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='static/attachments/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='civil_defense',
            field=models.FileField(blank=True, null=True, upload_to='static/civil_defenses/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='client_form',
            field=models.FileField(blank=True, null=True, upload_to='static/client_forms/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='deed',
            field=models.FileField(blank=True, null=True, upload_to='static/deeds/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='identity',
            field=models.FileField(blank=True, null=True, upload_to='static/identities/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='land_survey',
            field=models.FileField(blank=True, null=True, upload_to='static/land_surveys/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='old_license',
            field=models.FileField(blank=True, null=True, upload_to='static/old_licenses/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='soil_test',
            field=models.FileField(blank=True, null=True, upload_to='static/soil_tests/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='water_authority',
            field=models.FileField(blank=True, null=True, upload_to='static/water_authorities/'),
        ),
    ]
