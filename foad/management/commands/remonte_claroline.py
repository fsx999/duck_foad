# -*- coding: utf-8 -*-
import time
from django.db import IntegrityError
from mailrobot.models import Mail
from apogee.models import INS_ADM_ETP_IED
from django.core.mail import send_mail
from foad.models import FoadUser, FoadDip, FoadCour, FoadCourUser, CompteMail
from inscription.utils import make_ied_password
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    def handle(self, *args, **options):

        etape = ["L3NINF", "L2NINF", "L1NINF", "L3NDRO", "L2NDRO", "L1NDRO", "L3NEDU", "M2NEFI",
                 "M1NEFI", "L3NPSY", "L2NPSY", "L1NPSY", "M2NPCL", "M1NPCL", "M2NPST", "M1NPST",
                 "M2NPEA", "M1NPEA"]
        COURS = {}
        mail = Mail.objects.get(name='remontee')
        for e in etape:
            COURS[e] = [x[0] for x in FoadCour.objects.using('foad').filter(faculte=e).values_list('code')]
        cp = 0
        message = u"la remonté dans claroline s'est effectuée\n"
        erreur = False
        for inscription in INS_ADM_ETP_IED.inscrits.filter(COD_ETP__in=etape, remontee__in_plateforme=False):
        # for inscription in INS_ADM_ETP_IED.inscrits.filter(COD_ETP__in=etape):
            try:
            ##47I86

                cp += inscription.remontee_claroline(COURS, mail=mail)
                if not cp % 100:
                    time.sleep(2)
            except FoadDip.MultipleObjectsReturned:
                message += u"multi FoadDip %s %s\n" % (inscription.COD_IND.COD_ETU, inscription.COD_ETP)
            except IntegrityError:
                message += u"Integrity error %s %s\n" % (inscription.COD_ETP, inscription.COD_IND.COD_ETU)
            except UnicodeEncodeError:
                message += u"Unicode erreur %s\n" % inscription.COD_IND.COD_ETU
            except Exception, e:
                message += u"erreur %s \n" % e
        message += u"il y a eu %s mail envoyé" % cp
        send_mail("remontee claroline", message, 'nepasrepondre@iedparis8.net', ['paul.guichon@iedparis8.net'])
        print "fini"
