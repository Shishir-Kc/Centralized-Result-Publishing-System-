from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin






class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields to display in the user detail page
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('contact', 'account_status', 'grade', 'registered_school')}),
    )

    # Fields to show when creating a new user in admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('contact', 'account_status', 'grade', 'registered_school')}),
    )

    # Columns in the user list page
    list_display = ['username', 'email', 'account_status', 'is_staff', 'is_active']

admin.site.register(CustomUser, CustomUserAdmin)


"""
contact = models.IntegerField(verbose_name='Contact_number')
    account_status = models.CharField(choices=is_valid,name='Validated ? ')
    grade = models.OneToOneField(Grade,blank=True,null=True,on_delete=models.CASCADE)
    registered_school = models.ForeignKey(School,on_delete=models.CASCADE)
    


"""