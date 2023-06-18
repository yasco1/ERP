from django.db import models
from core.models import Gender, Religion, MartialStatus, MilitaryStatus, Nationalitie
from django.db.models import Max
from uuid import uuid4


class PersonalInfo(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    name_ar = models.CharField(
        max_length=100, verbose_name="Name (Arabic)", unique=True
    )
    name_en = models.CharField(
        max_length=100, verbose_name="Name (English)", unique=True
    )
    gender = models.ForeignKey(
        Gender, on_delete=models.CASCADE, related_name="Personal_Info"
    )
    insurance_id = models.CharField(
        max_length=50, unique=True, verbose_name="Insurance ID"
    )
    religion = models.ForeignKey(
        Religion, on_delete=models.CASCADE, related_name="Personal_Info"
    )
    martial_status = models.ForeignKey(
        MartialStatus,
        on_delete=models.CASCADE,
        related_name="PersonalInfo",
        verbose_name="Martial Status",
    )
    military_status = models.ForeignKey(
        MilitaryStatus,
        on_delete=models.CASCADE,
        related_name="PersonalInfo",
        verbose_name="Military Service Status",
    )
    birth_date = models.DateField(verbose_name="Birth Date")
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name_ar} - {self.name_en}"


class NationalID(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    nationality = models.ForeignKey(
        Nationalitie, on_delete=models.CASCADE, related_name="National_IDs"
    )
    personal_info = models.ForeignKey(
        PersonalInfo, on_delete=models.CASCADE, related_name="National_IDs", null=True
    )
    nationalId = models.CharField(max_length=50, unique=True)
    expire_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.nationalId}"


class MobileNumber(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    personal_info = models.ForeignKey(
        PersonalInfo, on_delete=models.CASCADE, related_name="MobileNumbers"
    )
    mobile_number = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.mobile_number}"


# class Educational_Info(models.Model):
#     uuid = models.UUIDField(
#         primary_key=True, default=uuid4, unique=True, editable=False
#     )
#     personal_info = models.ForeignKey(
#         Personal_Info, on_delete=models.CASCADE, related_name="Educational_Info"
#     )

#     def __str__(self) -> str:
#         return f"{self.personal}"


class Employment_Info(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    hr_code = models.BigIntegerField(verbose_name="HR Code", blank=True, null=False)
    personal_info = models.OneToOneField(
        PersonalInfo, on_delete=models.CASCADE, related_name="Employment_Info"
    )

    def save(self, *args, **kwargs):
        if self.hr_code is None:
            max_hrcode = Employment_Info.objects.aggregate(Max("hr_code"))[
                "hr_code__max"
            ]
            if max_hrcode is not None:
                self.hr_code = max_hrcode + 1
            else:
                self.hr_code = 1
        super(Employment_Info, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.personal_info}"


# class Department(models.Model):
#     uuid = models.UUIDField(
#         primary_key=True, default=uuid4, unique=True, editable=False
#     )
#     department = models.CharField(max_length=100)
#     department_manager = models.ForeignKey(
#         Employment_Info,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name="Departments",
#     )
#     is_active = models.BooleanField(default=True)


# class Employee_Status(models.Model):
#     uuid = models.UUIDField(
#         primary_key=True, default=uuid4, unique=True, editable=False
#     )
#     employee = models.ForeignKey(
#         Employment_Info, on_delete=models.CASCADE, related_name="Employee_Status"
#     )
#     notes = models.TextField(max_length=400)
#     is_active = models.BooleanField(default=True)
#     status_change_date = models.DateTimeField(auto_now_add=True)


# class Documentation(
#     models.Model,
# ):
#     def get_employee_images_filepath(self, filname):
#         return f"employees/{self.employee.hr_code}/{filname}"

#     uuid = models.UUIDField(
#         primary_key=True, default=uuid4, unique=True, editable=False
#     )
#     employee = models.ForeignKey(
#         Employment_Info, on_delete=models.CASCADE, related_name="Documentation"
#     )
#     profile_picture = models.ImageField(
#         max_length=255, upload_to=get_employee_images_filepath, null=True, blank=True
#     )
#     job_offer = models.ImageField(
#         max_length=255, upload_to=get_employee_images_filepath, null=True, blank=True
#     )
#     labor_picture = models.ImageField(
#         max_length=255, upload_to=get_employee_images_filepath, null=True, blank=True
#     )
#     birth_cert = models.ImageField(
#         max_length=255, upload_to=get_employee_images_filepath, null=True, blank=True
#     )
#     military_status = models.ImageField(
#         max_length=255, upload_to=get_employee_images_filepath, null=True, blank=True
#     )
#     insurance_picture = models.ImageField(
#         max_length=255, upload_to=get_employee_images_filepath, null=True, blank=True
#     )
#     id_picture = models.ImageField(
#         max_length=255, upload_to=get_employee_images_filepath, null=True, blank=True
#     )
#     education_picture = models.ImageField(
#         max_length=255, upload_to=get_employee_images_filepath, null=True, blank=True
#     )
