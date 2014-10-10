# -*- coding: utf-8 -*-
__author__ = 'paul'
from foad.models import FoadCour, FoadCourUser, FoadDip
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    def handle(self, *args, **options):
        etape = ["L3NINF", "L2NINF", "L1NINF", "L3NDRO", "L2NDRO", "L1NDRO", "L3NEDU", "M2NEFI",
                 "M1NEFI", "L3NPSY", "L2NPSY", "L1NPSY", "M2NPCL", "M1NPCL", "M2NPST", "M1NPST",
                 "M2NPEA", "M1NPEA"]
        #etape += ["DSNATA"]
        cours = FoadCour.objects.using('foad').filter(faculte__in=etape)
        cours = [x[0] for x in cours.values_list('code')]
        cours_user = FoadCourUser.objects.using('foad').filter(code_cours__in=cours, statut=5)
        users = [x[0] for x in cours_user.values_list('user')]
        dips = FoadDip.objects.using('foad').filter(user__in=users, user__statut=5)
        cours_user.using('foad').delete()
        dips.using('foad').delete()
        print cours_user.count()
        print dips.count()


