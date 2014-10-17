# -*- coding: utf-8 -*-
import time
from django.db import IntegrityError
from mailrobot.models import Mail
from datetime import date, datetime
from django.core.mail import send_mail
from django_apogee.models import InsAdmEtp
from foad.models import FoadUser, FoadDip, FoadCour, FoadCourUser, CompteMail, SettingsEtapeFoad
from django.core.management.base import BaseCommand
import os
from foad.utils import remontee_claroline


class Command(BaseCommand):
    def handle(self, *args, **options):
        now = datetime.now()
        etapes = list(SettingsEtapeFoad.objects.filter(date_ouverture__lt=now).values_list('cod_etp', flat=True))

        COURS = {}
        mail = Mail.objects.get(name='remontee')
        # for e in etapes:
        #     COURS[e] = [x[0] for x in FoadCour.objects.using('foad').filter(faculte=e).values_list('code')]
        cp = 0
        message = u"la remonté dans claroline s'est effectuée\n"
        erreur = False
        # # for inscription in InsAdmEtp.inscrits.filter(cod_etp__in=etape, remontee__in_plateforme=False):
        for inscription in InsAdmEtp.inscrits.filter(cod_etp__in=etapes):
            try:
                cp += remontee_claroline(inscription, COURS, mail=mail, email_perso='paul.guichon@iedparis8.net')
                if not cp % 100:
                    time.sleep(2)
            except FoadDip.MultipleObjectsReturned:
                message += u"multi FoadDip %s %s\n" % (inscription.cod_ind.cod_etu, inscription.cod_etp)
            except IntegrityError:
                message += u"Integrity error %s %s\n" % (inscription.cod_etp, inscription.cod_ind.cod_etu)
            except UnicodeEncodeError:
                message += u"Unicode erreur %s\n" % inscription.cod_ind.cod_etu
            except Exception, e:
                message += u"erreur %s \n" % e
        message += u"il y a eu %s mail envoyé" % cp
        send_mail("remontee claroline", message, 'nepasrepondre@iedparis8.net', ['paul.guichon@iedparis8.net'])
        print "fini"
