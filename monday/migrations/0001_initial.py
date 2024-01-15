# Generated by Django 4.2.7 on 2023-12-31 21:02

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(choices=[('Working on it', 'Working On It'), ('Done', 'Done')], max_length=100)),
                ('project_name', models.CharField(blank=True, max_length=100, null=True)),
                ('architectural_status', models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required')], max_length=100, null=True)),
                ('structural_status', models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required')], max_length=100, null=True)),
                ('plumbing_status', models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required')], max_length=100, null=True)),
                ('electrical_status', models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done'), ('Hold', 'Hold'), ('Not required', 'Not Required')], max_length=100, null=True)),
                ('sketch_approval_date', models.DateField(blank=True, null=True)),
                ('columns_approval_date', models.DateField(blank=True, null=True)),
                ('typeof_follow_up', models.CharField(blank=True, choices=[('Paper', 'Paper'), ('Municipal', 'Municipal')], max_length=100, null=True)),
                ('investor_affiliation', models.BooleanField(blank=True, null=True)),
                ('project_receipt_date', models.DateField(blank=True, null=True)),
                ('project_type', models.CharField(blank=True, choices=[('new', 'New'), ('addition', 'Addition'), ('restoration', 'Restoration')], max_length=100, null=True)),
                ('land_number', models.CharField(blank=True, max_length=100, null=True)),
                ('land_area', models.FloatField(blank=True, null=True)),
                ('project_location', models.CharField(blank=True, max_length=100, null=True)),
                ('project_number', models.IntegerField(blank=True, null=True)),
                ('sketch_design_progress_status', models.CharField(blank=True, choices=[('Ground floor', 'Ground'), ('First floor', 'First'), ('Second floor', 'Second'), ('Third floor', 'Third'), ('Annex room', 'Annex'), ('Facade', 'Facade')], max_length=100, null=True)),
                ('structural_design_start_date', models.DateField(blank=True, null=True)),
                ('structural_review', models.CharField(blank=True, choices=[('Working on it', 'Working On It'), ('Done', 'Done')], max_length=100, null=True)),
                ('structural_delivery_date', models.DateField(blank=True, null=True)),
                ('electrical_design_start_date', models.DateField(blank=True, null=True)),
                ('electrical_delivery_date', models.DateField(blank=True, null=True)),
                ('architectural_drawing_start_date', models.DateField(blank=True, null=True)),
                ('architectural_delivery_date', models.DateField(blank=True, null=True)),
                ('plumbing_design_start_date', models.DateField(blank=True, null=True)),
                ('plan_delivery_date', models.DateField(blank=True, null=True)),
                ('modification_price', models.FloatField(blank=True, null=True)),
                ('client_number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client', to='monday.client')),
                ('design_eng', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='designer', to=settings.AUTH_USER_MODEL)),
                ('electrical_eng_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='electrical_engineer', to=settings.AUTH_USER_MODEL)),
                ('structural_eng_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='structural_engineer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(blank=True, max_length=255, null=True)),
                ('written_at', models.DateField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('written_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('written_for', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='monday.project')),
            ],
        ),
    ]
