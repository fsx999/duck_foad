# -*- coding: utf-8 -*-
__author__ = 'paul'
from foad.models import FoadCour, FoadCourUser, FoadDip, SettingsEtapeFoad
from django.core.management.base import BaseCommand
from django.db import connections
from datetime import datetime, date
class Command(BaseCommand):
    def handle(self, *args, **options):
        now = datetime.now()
        etape = list(SettingsEtapeFoad.objects.filter(date_fermeture__lt=now, date_ouverture__gt=now).values_list('cod_etp', flat=True))
        cursor = connections['foad'].cursor()
        for x in etape:
            cursor.execute("""
            DELETE cl_cours_user FROM cl_cours_user INNER JOIN cl_cours ON cl_cours_user.code_cours=cl_cours.code and
             cl_cours.code IN (SELECT code from cl_cours WHERE faculte='%s') INNER JOIN cl_user ON cl_user.user_id=cl_cours_user.user_id and cl_user.statut=5;
            """ % x)
            cursor.execute("""
            DELETE cl_dip_user FROM cl_dip_user INNER JOIN cl_user WHERE cl_dip_user.user_id=cl_user.user_id and cl_user.statut=5 and cl_dip_user.dip_id='%s';
            """ % x)



