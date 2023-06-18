from django.db import models
from uuid import uuid4


class Countrie(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    country_name_en = models.CharField(max_length=100, unique=True)
    country_name_ar = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    collect_cvs = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.country_name_ar} - {self.country_name_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class Citie(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    city_name_en = models.CharField(max_length=100, unique=True)
    city_name_ar = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(
        Countrie, on_delete=models.CASCADE, related_name="cities"
    )
    collect_cvs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city_name_ar} - {self.city_name_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class District(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    district_name_en = models.CharField(max_length=100, unique=True)
    district_name_ar = models.CharField(max_length=100, unique=True)
    city = models.ForeignKey(Citie, on_delete=models.CASCADE, related_name="districts")
    collect_cvs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.district_name_ar} - {self.district_name_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class Region(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    region_name_en = models.CharField(max_length=100, unique=True)
    region_name_ar = models.CharField(max_length=100, unique=True)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="regions"
    )
    collect_cvs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.region_name_ar} - {self.region_name_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class Gender(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    gender_en = models.CharField(max_length=50, unique=True)
    gender_ar = models.CharField(max_length=50, unique=True)
    collect_cvs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.gender_ar} - {self.gender_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class Religion(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    religion_en = models.CharField(max_length=50, unique=True)
    religion_ar = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.religion_ar} - {self.religion_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class MartialStatus(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    martial_status_en = models.CharField(max_length=50, unique=True)
    martial_status_ar = models.CharField(max_length=50, unique=True)
    collect_cvs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.martial_status_ar} - {self.martial_status_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class MilitaryStatus(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    military_status_en = models.CharField(max_length=50, unique=True)
    military_status_ar = models.CharField(max_length=50, unique=True)
    collect_cvs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.military_status_ar} - {self.military_status_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class Nationalitie(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    nationality_en = models.CharField(max_length=50)
    nationality_ar = models.CharField(max_length=50)
    collect_cvs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.nationality_ar} - {self.nationality_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class Hierarcie(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    hierarcy_name_en = models.CharField(unique=True, max_length=100)
    hierarcy_name_ar = models.CharField(unique=True, max_length=100)
    hierarcy_number = models.IntegerField(unique=True)
    collect_cvs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hierarcy_name_ar} - {self.hierarcy_name_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class Jobtitle(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    jobtitle_en = models.CharField(unique=True, max_length=100)
    jobtitle_ar = models.CharField(unique=True, max_length=100)
    max_employees = models.IntegerField()
    collect_cvs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jobtitle_ar} - {self.jobtitle_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class NationalIDType(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    national_ID_type_en = models.CharField(unique=True, max_length=100)
    national_ID_type_ar = models.CharField(unique=True, max_length=100)
    collect_cvs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.national_ID_type_ar} - {self.national_ID_type_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class MobileNumberType(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    mobile_Number_Type_en = models.CharField(unique=True, max_length=100)
    mobile_Number_Type_ar = models.CharField(unique=True, max_length=100)
    collect_cvs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mobile_Number_Type_ar} - {self.mobile_Number_Type_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class EmployeeActivityStatus(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    status_en = models.CharField(unique=True, max_length=100)
    status_ar = models.CharField(unique=True, max_length=100)
    blacklist_from_applications = models.BooleanField(default=False)
    active_employee = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.status_ar} - {self.status_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class AttendanceStatus(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    Attendance_status_en = models.CharField(unique=True, max_length=100)
    Attendance_status_ar = models.CharField(unique=True, max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Attendance_status_ar} - {self.Attendance_status_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


# class Weekdays(models.Model):
#     uuid = models.UUIDField(
#         primary_key=True, default=uuid4, unique=True, editable=False
#     )
#     weekday_en = models.CharField(unique=True, max_length=100)
#     weekday_ar = models.CharField(unique=True, max_length=100)

#     def __str__(self):
#         return f"{self.weekday_ar} - {self.weekday_en}"

#     def delete(self, *args, **kwargs):
#         return  # delete is not allowed


class Qualification(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    qualification_en = models.CharField(unique=True, max_length=100)
    qualification_ar = models.CharField(unique=True, max_length=100)
    collect_cvs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.qualification_ar} - {self.qualification_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class Institute(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    institute_en = models.CharField(unique=True, max_length=100)
    institute_ar = models.CharField(unique=True, max_length=100)
    collect_cvs = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.institute_ar} - {self.institute_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class AnnualLeaveType(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    annual_leave_type_en = models.CharField(unique=True, max_length=100)
    annual_leave_type_ar = models.CharField(unique=True, max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.annual_leave_type_ar} - {self.annual_leave_type_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed


class InterviewTypes(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid4, unique=True, editable=False
    )
    interview_type_en = models.CharField(unique=True, max_length=100)
    interview_type_ar = models.CharField(unique=True, max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.interview_type_ar} - {self.interview_type_en}"

    def delete(self, *args, **kwargs):
        return  # delete is not allowed
