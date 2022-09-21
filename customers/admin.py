from django.contrib import admin
from .models import User, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    list_display = ['pkid','id', 'email', 'first_name', 'last_name']
    list_display_links= ['id', 'email']
    # add_form =CustomUserCreationForm
    # form = CustomUserChangeForm
    # model = User
    # exclude = ('date_joined',)
#     field_sets = (
#         (
#         _("Login Credentials"),
#         {
#             "fields":("email", "password",)
#         },
#         ),
#                 (
#             _("Personal Information"),
#             {
#                 "fields": (
#                     "first_name",
#                     "last_name",
#                 )
#             },
#         ),
#          (
#             _("Permission And Groups"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 )
#             },
#         ),
        
#     )
#     add_fieldsets = (
#     (
#         None,
#         {
#             "classes": ("wide",),
#             "fields": ("email", "password1", "password2", "is_staff", "is_active"),
#         },
#     ),
# )

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
