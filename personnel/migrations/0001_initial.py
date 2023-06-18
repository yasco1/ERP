# Generated by Django 4.2.2 on 2023-06-14 18:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name_ar', models.CharField(max_length=100, unique=True, verbose_name='Name (Arabic)')),
                ('name_en', models.CharField(max_length=100, unique=True, verbose_name='Name (English)')),
                ('insurance_id', models.CharField(max_length=50, unique=True, verbose_name='Insurance ID')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('address', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Personal_Info', to='core.gender')),
                ('martial_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PersonalInfo', to='core.martialstatus', verbose_name='Martial Status')),
                ('military_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PersonalInfo', to='core.militarystatus', verbose_name='Military Service Status')),
                ('religion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Personal_Info', to='core.religion')),
            ],
        ),
        migrations.CreateModel(
            name='NationalID',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nationalId', models.CharField(max_length=50, unique=True)),
                ('expire_date', models.DateField()),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='National_IDs', to='core.nationalitie')),
                ('personal_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='National_IDs', to='personnel.personalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='MobileNumber',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('mobile_number', models.CharField(max_length=15)),
                ('personal_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MobileNumbers', to='personnel.personalinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Employment_Info',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('hr_code', models.BigIntegerField(blank=True, verbose_name='HR Code')),
                ('personal_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Employment_Info', to='personnel.personalinfo')),
            ],
        ),
    ]