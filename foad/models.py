# coding=utf-8
import random
from django.db import models

# Create your models here.

####
#Acess à claroline
from django.utils.encoding import python_2_unicode_compatible
from mptt.models import MPTTModel, TreeForeignKey
from django_apogee.models import Etape, AnneeUni
from django_apogee.utils import make_etudiant_password


class FoadUser(models.Model):
    """

    """
    user_id = models.IntegerField(primary_key=True)
    statut = models.IntegerField(null=True)
    username = models.CharField(max_length=20, null=True)  # code étudiant pou run étudiant
    password = models.CharField(max_length=50, null=True)
    ied_code = models.CharField(max_length=8, null=True)
    email = models.CharField(max_length=100, null=True)
    nom = models.CharField(max_length=60, null=True)
    prenom = models.CharField(max_length=60, null=True)
    official_code = models.CharField(max_length=40, null=True, db_column='officialCode')
    phoneNumber = models.CharField(max_length=30, null=True)
    perso_email = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = 'cl_user'
        #managed = False

    def change_password(self, password=None):
        if password:
            self.password = password
        else:
            self.password = random.randrange(1000, 100000)
        self.save()

    def reset_password(self):
        try:
            self.password = make_etudiant_password(self.username)
            self.save()
        except ValueError:
            pass


class FoadDip(models.Model):
    user = models.ForeignKey(FoadUser, db_column='user_id', null=True)
    dip_id = models.CharField(max_length=20, null=True)

    def __unicode__(self):
        return self.dip_id

    class Meta:
        db_table = 'cl_dip_user'
        #managed = False


class FoadCourUser(models.Model):
    code_cours = models.CharField(max_length=40, primary_key=True, db_column='code_cours')
    user = models.ForeignKey(FoadUser, db_column='user_id')
    statut = models.IntegerField(default=5)
    role = models.CharField(max_length=60, null=True)
    team = models.IntegerField(default=0)
    tutor = models.IntegerField(default=0)

    class Meta:
        db_table = "cl_cours_user"
        #managed = False'


class FoadCour(models.Model):
    cours_id = models.IntegerField(primary_key=True, db_column='cours_id')
    code = models.CharField(max_length=40, null=True)
    fake_code = models.CharField(max_length=40, null=True)
    directory = models.CharField(max_length=20, null=True)
    dbName = models.CharField(max_length=40, null=True)
    languageCourse = models.CharField(max_length=15, null=True)
    faculte = models.CharField(max_length=12, null=True)
    intitule = models.CharField(max_length=250, null=True)
    visible = models.IntegerField( null=True)
    enrollment_key = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'cl_cours'


class CompteMail(models.Model):
    pw_name = models.EmailField(primary_key=True)

    class Meta:
        db_table = 'vpopmail'
        managed = False


@python_2_unicode_compatible
class SettingsEtapeFoad(Etape):
    date_fermeture = models.DateTimeField(null=True, blank=True)
    date_ouverture = models.DateTimeField(null=True, blank=True)
    vu_etape_inf = models.BooleanField(default=True)

    def __str__(self):
        return u'{} {}'.format(self.lib_etp, self.cod_etp)


@python_2_unicode_compatible
class EtapeMpttModel(MPTTModel):
    etape = models.OneToOneField(SettingsEtapeFoad, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __str__(self):
        return self.etape.lib_etp


@python_2_unicode_compatible
class SettingsAnneeFoad(AnneeUni):
    inscription = models.BooleanField(default=False)
    annee_en_cour = models.BooleanField(default=False)

    def __str__(self):
        if self.annee_en_cour:
            annee_en_cour = 'remontee ouverte'
        else:
            annee_en_cour = 'remontee fermée'
        return '{} {}'.format(self.cod_anu, annee_en_cour)
