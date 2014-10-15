# -*- coding: utf-8 -*-
__author__ = 'paul'
from foad.models import FoadCour, FoadCourUser, FoadDip
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        etape = ["L3NEDU",
        "L2NINF", "L1NINF", "L3NDRO", "L2NDRO", "L1NDRO", "L3NEDU", "M2NEFI",
                 "M1NEFI", "L3NPSY", "L2NPSY", "L1NPSY", "M2NPCL", "M1NPCL", "M2NPST", "M1NPST",
                 "M2NPEA", "M1NPEA"]
        etape += ["DSNATA"]

        cours = list(FoadCour.objects.using('foad_test').filter(faculte__in=etape).values_list('code', flat=True))
        cours_user = FoadCourUser.objects.using('foad_test').exclude(statut__in=[3,1,2], user__statut__in=[3,1,2])
        users = [x[0] for x in cours_user.values_list('user')]
        dips = FoadDip.objects.using('foad').filter(user__in=users)
        cours_user.using('foad_test').delete()
        dips.using('foad_test').delete()
        print cours_user.count()
        print dips.count()


