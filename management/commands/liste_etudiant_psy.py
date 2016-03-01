# -*- coding: utf-8 -*-
import csv
from django.core.management.base import BaseCommand
from django_apogee.models import InsAdmEtpInitial


class Command(BaseCommand):
    def handle(self, *args, **options):

        result = [[ins.cod_ind.lib_nom_pat_ind, ins.cod_ind.lib_pr1_ind, ins.cod_ind.cod_etu, ins.cod_etp] for ins in InsAdmEtpInitial.inscrits.using('oracle').filter(cod_etp__in=['L1NPSY',
                                                                                       'L2NPSY',
                                                                                       'L3NPSY'], cod_anu=2015).order_by('cod_ind__lib_nom_pat_ind')]


        with open('/vagrant/liste_etu.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            champs = ['nom', 'prenom', 'code etudiant', 'etape']
            spamwriter.writerow(champs)
            for row in result:
                spamwriter.writerow(row)
