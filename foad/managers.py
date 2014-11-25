# coding=utf-8
from __future__ import unicode_literals
from django.db import models


class AuditeurManager(models.Manager):

    def create_auditeur(self, individu):
        return self.get_or_create(
            last_name=individu.last_name,
            first_name=individu.first_name1,
            personal_email=individu.personal_email,
            address=individu.get_adresse_annuelle_simple(),
            phone_number=individu.adresses.get(type=1).listed_number,
            code_ied=str(individu.code_opi) + 'B',
            birthday=individu.birthday,
            annee_id=individu.annee
        )
