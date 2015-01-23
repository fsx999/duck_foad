# coding=utf-8
from django_apogee.models import Individu
from django.core.mail import EmailMessage
from django.utils import translation
import os
from django.template.loader import render_to_string
from django.template.defaultfilters import date as _date
from django.conf import settings
from foad.utils import email_ied

__author__ = 'paul'
from django.core.management.base import BaseCommand
from xhtml2pdf import pdf as pisapdf
from xhtml2pdf import pisa
from settings import BASE_DIR
import xlrd
import time
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        fichier = settings.BASE_DIR + '/l2.xls'
        texte = u"""
        Ci-joint votre convocation aux regoupements

        Ceci est un email automatique.\n
        Veuillez ne pas y répondre.
        """
        template = "convocation/convocation_l2.html"
        objects = u"[IED] CONVOCATION AUX REGROUPEMENTS"
        num_etu = 0
        self.deroulement = None
        # self.deroulement = settings.PROJECT_DIR + '1.pdf'
        self.publipostage(fichier, template, texte, num_etu, objects)

    def date(self, date):
        date = xlrd.xldate_as_tuple(date, 0)
        return _date(datetime(date[0], date[1], date[2]), "l d F o")

    def publipostage(self, fichier, template, texte, num_etu, objects):
        wb = xlrd.open_workbook(os.path.join(BASE_DIR, fichier))
        sh = wb.sheet_by_index(0)
        translation.activate(settings.LANGUAGE_CODE)
        i = 0
        for rownum in range(sh.nrows):
            i += 1
            if rownum == 0:
                continue

            if sh.cell(rownum, 0).value == "":
                break
            values = sh.row_values(rownum)
            cod_etu = int(values[num_etu])
            context = {'static': os.path.join(BASE_DIR, 'documents/static/images/').replace('\\', '/')}

            context['num_group'] = int(values[1])

            context['date_1'] = self.date(values[3])
            context['salle_1'] = int(values[2])
            context['date_2'] = self.date(values[5])
            context['salle_2'] = int(values[4])

            individu = Individu.objects.get(cod_etu=cod_etu)
            f = open('convocation.pdf', 'wb')

            context['individu'] = individu
            pdf = pisapdf.pisaPDF()
            pdf.addDocument(pisa.CreatePDF(render_to_string(template, context)))  # on construit le pdf
            if self.deroulement:
                pdf.addFromFile(self.deroulement)

            pdf.join(f)
            liste_email = [individu.get_email(2014), email_ied(individu), 'convocations@iedparis8.net'] if not settings.DEBUG else ['nepasrepondre@iedparis8.net']
            email = EmailMessage(subject=objects, body=texte, from_email='nepasrepondre@iedparis8.net',
                                 to=liste_email)

            f.close()

            f = open('convocation.pdf', 'r')
            email.attach(filename='convocation_regoupement.pdf', content=f.read())
            email.send()
            print "email envoyé à %s" % individu.cod_etu
            if i == 100:
                time.sleep(5)
                i = 0

            f.close()
            if settings.DEBUG:
                if rownum == 1:
                    break
        print "fini"
