# -*- coding: utf-8 -*-
import datetime
from django.db.utils import OperationalError
from inscription.models import Step

__author__ = 'paul'
from django.core.management.base import BaseCommand
from foad.utils import open_cour


class Command(BaseCommand):

    def dictfetchall(self, cursor):
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]

    def handle(self, *args, **options):
        cours = [
            'ECEPDESU',
            'ECEPLSC',
            'ECEPMSC',
            'ECEPLI',
            'ECEPLD',
            'ECEPMC',
            'ECEPMD',
            'ECEPMS'
        ]
        for cour in cours:
            try:
                open_cour(cour)
                print u"Le cour %s est crée" % cour
            except OperationalError:
                print u"Le cour %s est déjà crée" % cour
