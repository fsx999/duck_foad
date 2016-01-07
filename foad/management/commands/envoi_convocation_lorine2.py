# -*- coding: utf8 -*-
import datetime
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django_apogee.models import InsAdmEtpInitial, Etape
from pprint import pprint
import os
from django.conf import settings
from duck_utils.utils import make_pdf, get_email_envoi


class Command(BaseCommand):
    help = "Envoi convocation regroupements"

    def handle(self, *args, **options):
        mail_body = u"""
        Annule et remplace le précédent envoi.

        Ci-joint votre convocation aux regroupements

        Ceci est un email automatique.\n
        Veuillez ne pas y répondre.

        Les 2 sessions de janvier et mars sont obligatoires.
        Si vous êtes en 2e année et que vous avez assisté lors de votre première année
        de master 2 à ces regroupements ils ne sont pas obligatoires pour vous
        cette année.
        """
        template = "convocation/m2_laurine.html"
        mail_subject = u"[IED] CONVOCATION AUX REGROUPEMENTS (CORRECTIF)"
        # Numero Etudiant;Nom patronimique;Prénom:;Email perso;Email Foad;groupe

        csv_filename = settings.BASE_DIR + '/M2_2015-1.csv'

        destinataires = []
        with open(csv_filename, 'r') as f:
            for l in f.readlines():
                num_etu, nom, prenom, email_perso, email_foad, groupe = l.split(';')
                destinataires.append(
                    {
                        'num_etu': num_etu,
                        'nom': nom,
                        'prenom': prenom,
                        'email_perso': email_perso,
                        'email_foad': email_foad,
                        'groupe': groupe.rstrip()
                    }
                )
        #print destinataires
        self.publipostage(template, mail_subject, mail_body, destinataires)

    def publipostage(self, template, mail_subject, mail_body, destinataires):
        mois_dict = {
            1: 'janvier',
            2: 'février',
            3: 'mars',
            4: 'avril',
            5: 'mai',
            6: 'juin',
            7: 'juillet',
            8: 'août',
            9: 'septembre',
            10: 'octobre',
            11: 'novembre',
            12: 'décembre',
        }

        now = datetime.datetime.now()
        debug_count = 0
        for d in destinataires:
            email = EmailMessage(mail_subject, mail_body, from_email="nepasrepondre@iedparis8.net",
                                 to=[get_email_envoi(d['email_perso']),
                                     get_email_envoi(d['email_foad'])])
            context = dict(d)
            context['static'] = os.path.join(settings.BASE_DIR,
                                             '..',
                                             'duck_inscription', 'duck_inscription',
                                             'static', 'images')
            context.update({'jour': str(now.day),
                            'mois': mois_dict[now.month],
                            'annee': str(now.year)})


            context['date_regroupement'] = "13 janvier au 15 janvier 2016"
            f = make_pdf(template, context)
            email.attach('convocation1.pdf', f, 'application/pdf')

            context['date_regroupement'] = "09 mars au 11 mars 2016"
            f = make_pdf(template, context)
            email.attach('convocation2.pdf', f, 'application/pdf')

            email.send()

            if settings.DEBUG:
                debug_count += 1
                if debug_count == 10:
                    break