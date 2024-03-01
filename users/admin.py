from django.contrib import admin
from .models import User, UserConfirmation, CODE_VERIFIED
# from ..app.models import UserCourse


# class UserCourseInline(admin.TabularInline):
#     model = UserCourse


# @admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # inlines = [UserCourseInline]
    list_display = ("id", "phone", "is_active", "is_staff", "is_superuser", 'is_code_verified', 'code')
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("phone",)
    list_display_links = ("id", "phone")

    def is_code_verified(self, obj):
        return obj.auth_status == CODE_VERIFIED

    def code(self, obj):
        if obj.verify_codes.all().last():
            return obj.verify_codes.all().last().code
        return None

    code.short_description = 'Kod'
    is_code_verified.short_description = 'Tasdiqlanganmi?'


admin.site.register(User, UserAdmin)
