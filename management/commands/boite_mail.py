# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django_apogee.utils import make_etudiant_password
import unicodedata
from mailrobot.models import Mail
from foad.models import CompteMail
from django.core.management.base import BaseCommand
from django_apogee.models import InsAdmEtpInitial
import os
from django.core.mail import send_mail
class Command(BaseCommand):
    def handle(self, *args, **options):
        mail = Mail.objects.get(name='remontee')
        cod_etps = [
            'L3NEDU',
            'M1NEFI',
            'L1NDRO',
            'L2NDRO',
            'L3NDRO',
            'L1NPSY',
            'L2NPSY',
            'L3NPSY',
            'L1NINF',
            'L2NINF',
            'L3NINF',
            'DSNPCA',
            'M1NPCL',
            'M2NPCL',
            'M1NPEA',
            'M2NPEA',
            'M1NPST',
            'M2NPST',
        ]
        for code_etud in InsAdmEtpInitial.inscrits.using('oracle').filter(cod_etp__in=cod_etps, cod_anu=2015):
            individu = code_etud.cod_ind
            cod = individu.lib_pr1_ind.replace(" ", "\\ ").replace("'", "\\'").replace("`", "") + '-' + individu.lib_nom_pat_ind.replace(" ", "\\ ").replace("'", "\\'").replace('(', '').replace(')', '').replace("`", "")
            cod = unicodedata.normalize('NFKD', unicode(cod)).encode("ascii", "ignore").upper()
            password = make_etudiant_password(individu.cod_etu)
            email = unicode(individu.cod_etu)+'@foad.iedparis8.net'
            # email = 'nepasrepondre@iedparis8.net'
            if email:
                if not CompteMail.objects.using('vpopmail').filter(pw_name=individu.cod_etu):

                    command = u'/home/ied-www/bin/vadduser  -q 2000000000 -c "%s" %s %s' % (
                        cod,
                        email,
                        password

                    )

                    os.system(command)
                    context = {
                            'etape': str(code_etud.cod_etp),
                            'prenom': str(individu.lib_pr1_ind),
                            'username': str(individu.cod_etu),
                            'password': str(password),
                            'email': str(email)
                        }

                    r = mail.make_message(
                        sender='nepasrepondre@iedparis8.net',
                        recipients=(individu.get_email(2015), email),
                        context=context
                    )
                    r.send()
        print "fini"
