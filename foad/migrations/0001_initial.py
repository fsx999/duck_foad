# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_apogee', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompteMail',
            fields=[
                ('pw_name', models.EmailField(max_length=75, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'vpopmail',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuditeurLibreApogee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=30, verbose_name=b'Nom')),
                ('first_name', models.CharField(max_length=30, verbose_name=b'Prenom')),
                ('personal_email', models.EmailField(max_length=200, verbose_name=b'email personnel')),
                ('address', models.CharField(max_length=200, verbose_name=b'adresse')),
                ('phone_number', models.CharField(default=None, max_length=15, null=True, verbose_name=b'num\xc3\xa9ro de t\xc3\xa9l\xc3\xa9phone')),
                ('code_ied', models.CharField(max_length=8, verbose_name=b'code ied')),
                ('status_modified', models.BooleanField(default=True)),
                ('access_claroline', models.BooleanField(default=True, verbose_name=b'Acc\xc3\xa8s \xc3\xa0 claroline')),
                ('date_registration_current_year', models.DateField(auto_now_add=True)),
                ('birthday', models.DateField(verbose_name=b'Date de naissance')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EtapeMpttModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoadCour',
            fields=[
                ('cours_id', models.IntegerField(serialize=False, primary_key=True, db_column=b'cours_id')),
                ('code', models.CharField(max_length=40, null=True)),
                ('fake_code', models.CharField(max_length=40, null=True)),
                ('directory', models.CharField(max_length=20, null=True)),
                ('dbName', models.CharField(max_length=40, null=True)),
                ('languageCourse', models.CharField(max_length=15, null=True)),
                ('faculte', models.CharField(max_length=12, null=True)),
                ('intitule', models.CharField(max_length=250, null=True)),
                ('visible', models.IntegerField(null=True)),
                ('enrollment_key', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'cl_cours',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoadCourUser',
            fields=[
                ('code_cours', models.CharField(max_length=40, serialize=False, primary_key=True, db_column=b'code_cours')),
                ('statut', models.IntegerField(default=5)),
                ('role', models.CharField(max_length=60, null=True)),
                ('team', models.IntegerField(default=0)),
                ('tutor', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'cl_cours_user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoadDip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dip_id', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'cl_dip_user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoadUser',
            fields=[
                ('user_id', models.IntegerField(serialize=False, primary_key=True)),
                ('statut', models.IntegerField(null=True)),
                ('username', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('ied_code', models.CharField(max_length=8, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('nom', models.CharField(max_length=60, null=True)),
                ('prenom', models.CharField(max_length=60, null=True)),
                ('official_code', models.CharField(max_length=40, null=True, db_column=b'officialCode')),
                ('phoneNumber', models.CharField(max_length=30, null=True)),
                ('perso_email', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'cl_user',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Remontee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remontee', models.BooleanField(default=False)),
                ('in_plateforme', models.BooleanField(default=False)),
                ('is_valide', models.BooleanField(default=False)),
                ('etape', models.OneToOneField(related_name='remontee', to='django_apogee.InsAdmEtp')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SettingsAnneeFoad',
            fields=[
                ('anneeuni_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='django_apogee.AnneeUni')),
                ('inscription', models.BooleanField(default=False)),
                ('annee_en_cour', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=('django_apogee.anneeuni',),
        ),
        migrations.CreateModel(
            name='SettingsEtapeFoad',
            fields=[
                ('etape_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='django_apogee.Etape')),
                ('date_fermeture', models.DateTimeField(null=True, blank=True)),
                ('date_ouverture', models.DateTimeField(null=True, blank=True)),
                ('vu_etape_inf', models.BooleanField(default=True)),
                ('c2i', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=('django_apogee.etape',),
        ),
        migrations.AddField(
            model_name='foaddip',
            name='user',
            field=models.ForeignKey(db_column=b'user_id', to='foad.FoadUser', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='foadcouruser',
            name='user',
            field=models.ForeignKey(to='foad.FoadUser', db_column=b'user_id'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='etapempttmodel',
            name='etape',
            field=models.OneToOneField(related_name='mptt', to='foad.SettingsEtapeFoad'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='etapempttmodel',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='foad.EtapeMpttModel', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='auditeurlibreapogee',
            name='annee',
            field=models.ForeignKey(to='django_apogee.AnneeUni'),
            preserve_default=True,
        ),
    ]
