from django.contrib import admin
from .models import Profile, Ruc, Contributor, Ficharuc, Schedule, Tax

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class RucAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ContributorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class FicharucAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ScheduleAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class TaxAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Ruc, RucAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Ficharuc, FicharucAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Tax, TaxAdmin)