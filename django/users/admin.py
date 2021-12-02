from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from django.db import models
from .models import NewUser


class UserAdminConfig(UserAdmin):
    model = NewUser
    
    search_field = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ['-start_date', ]
    
    list_display = (
        'email', 'user_name', 'first_name', 'is_active', 'is_staff'
    )
    
    fieldsets = ((None, {
        'fields': ('email', 'user_name', 'first_name', )
        }),
                 
        ('Permissions', {
            'fields': ('is_staff', 'is_active')
        }),
        
        ('Personal', {
            'fields': ('about', )
        }),
    )
    
    # adds custom widgets for a certain field
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={
                'rows': 20, 
                'cols': 60
            })
        },
    }
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'user_name',
                'first_name',
                'password1',
                'password2',
                'is_active',
                'is_staff',
            )
        }),
    )
    
admin.site.register(NewUser, UserAdminConfig)