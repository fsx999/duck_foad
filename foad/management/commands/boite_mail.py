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
        text = """
Bonjour {prenom} ,


Nous avons le plaisir de vous annoncer que votre inscription en {etape} est validée.
Vous recevrez dans les meilleurs délais votre carte d’étudiant de l’Université de Paris 8

Votre code étudiant : {username}
Votre mot de passe : {{password}}

Par ailleurs, un service de messagerie Web vous est accordé pour toute correspondance pédagogique.
Vous pourrez vous y authentifier avec les informations ci-dessous pour y avoir accès.

L'accès à votre messagerie : https://webmail-foad.iedparis8.net/
Votre nom d'utilisateur : {email}
Votre mot de passe : {password}

{email} est votre adresse électronique et devra être utilisée exclusivement pour les échanges avec vos enseignants et le secrétariat de votre formation.

Veillez bien à consulter régulièrement votre messagerie afin de suivre l'actualité de votre enseignement à distance.

Cordialement.

        """
        for code_etud in InsAdmEtpInitial.inscrits.using('oracle').filter(cod_etp='L3NEDU', cod_anu=2015):
            individu = code_etud.cod_ind
            cod = individu.lib_pr1_ind.replace(" ", "\\ ").replace("'", "\\'").replace("`", "") + '-' + individu.lib_nom_pat_ind.replace(" ", "\\ ").replace("'", "\\'").replace('(', '').replace(')', '').replace("`", "")
            cod = unicodedata.normalize('NFKD', unicode(cod)).encode("ascii", "ignore").upper()
            password = make_etudiant_password(individu.cod_etu)
            email = str(individu.cod_etu)+'@foad.iedparis8.net',
            print cod, email, password
            # email = 'nepasrepondre@iedparis8.net'
            if not CompteMail.objects.using('vpopmail').filter(pw_name=individu.cod_etu):

                command = u'/home/ied-www/bin/vadduser  -q 2000000000 -c "%s" %s %s' % (
                    cod,
                    email,
                    password

                )

                os.system(command)
            m = text.format(etape=str(code_etud.cod_etp),
                    prenom= str(individu.lib_pr1_ind),
                    username = str(individu.cod_etu),
                    password = str(password),
                    email= str(email))

            object = "[IED] identifiant"
            send_mail(object, m, 'nepasrepondre@iedparis8.net', [email])
            print individu.cod_etu
        print "fini"
