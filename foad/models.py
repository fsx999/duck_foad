# coding=utf-8
import random
from django.db import models

# Create your models here.

####
#Acess à claroline
from django.utils.encoding import python_2_unicode_compatible
from mptt.models import MPTTModel, TreeForeignKey
from django_apogee.models import Etape, AnneeUni, InsAdmEtp
from django_apogee.utils import make_etudiant_password
from foad.managers import AuditeurManager


class FoadUser(models.Model):
    """

    """
    user_id = models.IntegerField(primary_key=True)
    statut = models.IntegerField(null=True)
    username = models.CharField(max_length=20, null=True)  # code étudiant pour un étudiant
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
    c2i = models.BooleanField(default=False)

    def __str__(self):
        return u'{} {}'.format(self.lib_etp, self.cod_etp)


@python_2_unicode_compatible
class EtapeMpttModel(MPTTModel):
    etape = models.OneToOneField(SettingsEtapeFoad, unique=True, related_name='mptt')
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


class Remontee(models.Model):
    remontee = models.BooleanField(default=False)
    in_plateforme = models.BooleanField(default=False)
    is_valide = models.BooleanField(default=False)
    etape = models.OneToOneField(InsAdmEtp, related_name="remontee")


@python_2_unicode_compatible
class AuditeurLibreApogee(models.Model):
    last_name = models.CharField("Nom", max_length=30)
    first_name = models.CharField("Prenom", max_length=30)
    personal_email = models.EmailField("email personnel", max_length=200)
    address = models.CharField("adresse", max_length=200)
    phone_number = models.CharField("numéro de téléphone", max_length=15, null=True, default=None)
    code_ied = models.CharField('code ied', max_length=8)
    status_modified = models.BooleanField(default=True)
    access_claroline = models.BooleanField("Accès à claroline", default=True)
    date_registration_current_year = models.DateField(auto_now_add=True)
    birthday = models.DateField("Date de naissance")
    annee = models.ForeignKey(AnneeUni)
    objects = AuditeurManager()

    def get_email(self, annee):
        return self.personal_email

    def __str__(self):
        return self.last_name + ' ' + self.first_name
