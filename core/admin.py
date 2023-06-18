from django.contrib import admin
from .models import (
    Countrie,
    Citie,
    District,
    Region,
    Gender,
    Religion,
    MartialStatus,
    MilitaryStatus,
    Nationalitie,
    Hierarcie,
    Jobtitle,
    NationalIDType,
    MobileNumberType,
    EmployeeActivityStatus,
    AttendanceStatus,
    Qualification,
    Institute,
    AnnualLeaveType,
    InterviewTypes,
)

admin.site.register(Countrie)
admin.site.register(Citie)
admin.site.register(District)
admin.site.register(Region)
admin.site.register(Gender)
admin.site.register(Religion)
admin.site.register(MartialStatus)
admin.site.register(MilitaryStatus)
admin.site.register(Nationalitie)
admin.site.register(Hierarcie)
admin.site.register(Jobtitle)
admin.site.register(NationalIDType)
admin.site.register(MobileNumberType)
admin.site.register(EmployeeActivityStatus)
admin.site.register(AttendanceStatus)
admin.site.register(Qualification)
admin.site.register(Institute)
admin.site.register(AnnualLeaveType)
admin.site.register(InterviewTypes)