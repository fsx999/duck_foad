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
        Ci-joint votre convocation aux regroupements

        Ceci est un email automatique.\n
        Veuillez ne pas y répondre.
        """
        template = "convocation/m1_laurine.html"
        mail_subject = u"[IED] CONVOCATION AUX REGROUPEMENTS"


        destinataires = []
        for  i in InsAdmEtpInitial.inscrits.filter(cod_etp="M1NPCL", nbr_ins_etp=1):
            destinataires.append({'nom': ' '.join([i.cod_ind.lib_nom_pat_ind,
                                                   i.cod_ind.lib_nom_usu_ind]),
                                  'prenom': ' '.join([i.cod_ind.lib_pr1_ind,
                                                     i.cod_ind.lib_pr2_ind,
                                                     i.cod_ind.lib_pr3_ind]),
                                  'num_etu': str(i.cod_ind.cod_etu),
                                  'email': i.cod_ind.get_email(2015)})

        self.publipostage(template, mail_subject, mail_body, destinataires)
        # print sorted([e.cod_etp for e in Etape.objects.all()
        #               if e.cod_etp[0] == 'M' and e.cod_etp.endswith('PCL')])

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
            context = dict(d)
            context['static'] = os.path.join(settings.BASE_DIR,
                                             '..',
                                             'duck_inscription', 'duck_inscription',
                                             'static', 'images')
            context.update({'jour': str(now.day),
                            'mois': mois_dict[now.month],
                            'annee': str(now.year)})
            print context
            f = make_pdf(template, context)
            # convocation_html_filename = settings.BASE_DIR+'convocation.html'
            # convocation_pdf_filename = '/home/vagrant/PycharmProjects/duck_site/convocation.pdf'
            # Creation du fichier html
            # f = open(convocation_html_filename, 'wb')
            # f.write(render_to_string(template, context))
            # f.close()
            # Conversion du fichier html en pdf
            # os.system("{prog_name} {source} {dest}".format(prog_name='/usr/local/bin/wkhtmltopdf',
            #                                                source=convocation_html_filename,
            #                                                dest=convocation_pdf_filename))
            # Creation et Envoi du mail avec la PJ
            email = EmailMessage(mail_subject, mail_body, from_email="noreply@iedparis8.net",
                                 to=[get_email_envoi(d['email'])])
            # f = open(convocation_pdf_filename)
            email.attach('convocation.pdf', f, 'application/pdf')
            email.send()
            # f.close()
            # Clean
            # os.remove(convocation_html_filename)
            # os.remove(convocation_pdf_filename)
            if settings.DEBUG:
                debug_count += 1
                if debug_count == 10:
                    break