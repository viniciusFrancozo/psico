from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Pessoa, Psicologo


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username','id',)
    search_fields = ('email','id',)
    fieldsets = (
        (None, {'fields': (
            'email',
            'password',
            'username',
            'first_name',
            'last_name',
        )}),
        ('Permissions', {'fields': ('is_admin','is_staff','is_superuser','is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ()
    filter_vertical = ()

admin.site.register(Account, AccountAdmin)

@admin.register(Pessoa)
class ConsultasAdmin(admin.ModelAdmin):
    list_display = ('pessoa_id',)

@admin.register(Psicologo)
class ConsultasAdmin(admin.ModelAdmin):
    list_display = ('psicologo_id',)
