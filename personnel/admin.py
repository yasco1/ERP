from django.contrib import admin
from .models import (
    PersonalInfo,
    Employment_Info,
    NationalID,
    MobileNumber,
)

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(Employment_Info)
admin.site.register(NationalID)
admin.site.register(MobileNumber)
