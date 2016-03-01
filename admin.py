# coding=utf-8
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import MPTTModelAdmin
from foad.models import FoadDip, FoadUser, EtapeMpttModel


class FoadDipUserAdmin(admin.TabularInline):
    model = FoadDip
    extra = 0
    can_delete = False
    #def has_add_permission


class FoadUserAdmin(admin.ModelAdmin):
    inlines = [FoadDipUserAdmin]
    search_fields = ('username', 'nom', 'prenom')


admin.site.register(FoadUser, FoadUserAdmin)
admin.site.register(EtapeMpttModel, DjangoMpttAdmin)
