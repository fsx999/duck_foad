# -*- coding: utf-8 -*-
import time
from django.db import IntegrityError
from mailrobot.models import Mail
from datetime import date, datetime
from django.core.mail import send_mail
from django_apogee.models import InsAdmEtp
from django_apogee.utils import make_etudiant_password
from foad.models import FoadUser, FoadDip, FoadCour, FoadCourUser, CompteMail, SettingsEtapeFoad, Remontee, \
    AuditeurLibreApogee
from django.core.management.base import BaseCommand
import os
from foad.utils import remontee_claroline


class Command(BaseCommand):
    def handle(self, *args, **options):
        now = datetime.now()
        etapes = SettingsEtapeFoad.objects.filter(date_ouverture__lt=now)
        print "coucuo"
        COURS = {}
        mail = Mail.objects.get(name='remontee')
        for e in list(etapes.values_list('cod_etp', flat=True)):
            COURS[e] = [x[0] for x in FoadCour.objects.using('foad').filter(faculte=e).values_list('code')]
        cp = 0
        message = u"la remonté dans claroline s'est effectuée\n"
        for x in InsAdmEtp.inscrits.filter(remontee__isnull=True):
            Remontee.objects.create(etape=x)
        for etape in etapes:
            etps = list(etape.mptt.get_descendants(include_self=True).values_list('etape__cod_etp', flat=True))
            c2i = etape.c2i
            cod_etp = etape.cod_etp
            for inscription in InsAdmEtp.inscrits.filter(cod_etp=cod_etp, remontee__remontee=False):
            # for inscription in InsAdmEtp.inscrits.filter(cod_etp=cod_etp):
                try:
                    cp += remontee_claroline(inscription, etps, c2i, 'foad', COURS, mail=mail, envoi_mail=True)
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
                print message

        for auditeur in AuditeurLibreApogee.objects.filter(status_modified=True):
        # for auditeur in AuditeurLibreApogee.objects.all():
            auditeur.cod_etp = 'L1NPSY'
            auditeur.cod_ind = auditeur
            auditeur.cod_etu = auditeur.code_ied
            auditeur.cod_anu = 2014
            cp += remontee_claroline(auditeur, [u'L1NPSY'], False, 'foad', COURS, auditeur=True, envoi_mail=True)
            auditeur.status_modified = False
            auditeur.save()
        message += u"il y a eu %s mail envoyé" % cp
        send_mail("remontee claroline", message, 'nepasrepondre@iedparis8.net', ['paul.guichon@iedparis8.net'])
        print "fini"


# def save_auditeur(auditeur, user_foad, db):
#     user_foad.email = auditeur.code_ied + '@foad.iedparis8.net'
#     user_foad.nom = auditeur.last_name
#     user_foad.prenom = auditeur.first_name
#     user_foad.statut = 5
#     user_foad.official_code = auditeur.code_ied
#     user_foad.password = make_etudiant_password(auditeur.code_ied[:-1])
#     user_foad.save(using=db)  # création de l'user
#     return user_foad
