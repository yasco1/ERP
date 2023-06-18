from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = (
            "username",
            "email",
            "password",
            "is_HR",
            "is_PR",
        )  # Add email field to fields


class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "employee",
                    "is_HR",
                    "is_PR",
                ),
            },
        ),
    )
    list_display = ("email", "employee", "is_superuser", "is_HR", "is_PR", "is_active")
    search_fields = (
        "email",
        "employee__name_ar",
        "is_HR",
        "is_PR",
    )
    readonly_fields = ("id",)

    filter_horizontal = ()
    list_filter = ("email", "employee", "is_active")
    fieldsets = ()
    ordering = ("email", "employee", "is_superuser", "is_HR", "is_PR", "is_active")


admin.site.register(Account, AccountAdmin)
