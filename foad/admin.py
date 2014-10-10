# coding=utf-8
from django.contrib import admin
from foad.models import FoadDip, FoadUser


class FoadDipUserAdmin(admin.TabularInline):
    model = FoadDip
    extra = 0
    can_delete = False
    #def has_add_permission


class FoadUserAdmin(admin.ModelAdmin):
    inlines = [FoadDipUserAdmin]
    search_fields = ('username', 'nom', 'prenom')


admin.site.register(FoadUser, FoadUserAdmin)
