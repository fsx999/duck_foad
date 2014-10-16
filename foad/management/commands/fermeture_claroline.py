# -*- coding: utf-8 -*-
__author__ = 'paul'
from foad.models import FoadCour, FoadCourUser, FoadDip
from django.core.management.base import BaseCommand
from django.db import connections

class Command(BaseCommand):
    def handle(self, *args, **options):
        etape = ["M2NPCL",
        "L2NINF", "L1NINF", "L3NDRO", "L2NDRO", "L1NDRO", "L3NEDU", "M2NEFI",
                 "M1NEFI", "L3NPSY", "L2NPSY", "L1NPSY", "M2NPCL", "M1NPCL", "M2NPST", "M1NPST",
                 "M2NPEA", "M1NPEA"]
        # etape += ["DSNATA"]
        cursor = connections['foad_test'].cursor()
        for x in etape:
            cursor.execute("""
            DELETE cl_cours_user FROM cl_cours_user INNER JOIN cl_cours ON cl_cours_user.code_cours=cl_cours.code and
             cl_cours.code IN (SELECT code from cl_cours WHERE faculte='%s') INNER JOIN cl_user ON cl_user.user_id=cl_cours_user.user_id and cl_user.statut=5;
            """ % x)
            cursor.execute("""
            DELETE cl_dip_user FROM cl_dip_user INNER JOIN cl_user WHERE cl_dip_user.user_id=cl_user.user_id and cl_user.statut=5and cl_dip_user.dip_id='%s';
            """ % x)


        # dips = FoadDip.objects.using('foad_test').filter(user__in=users)
        # cours_user.using('foad_test').delete()
        # dips.using('foad_test').delete()
        # print cours_user.count()
        # print dips.count()


