# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EtapeMpttModel'
        db.create_table(u'foad_etapempttmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('etape', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['foad.SettingsEtapeFoad'], unique=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['foad.EtapeMpttModel'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'foad', ['EtapeMpttModel'])

        # Adding field 'SettingsEtapeFoad.vu_etape_inf'
        db.add_column(u'foad_settingsetapefoad', 'vu_etape_inf',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'EtapeMpttModel'
        db.delete_table(u'foad_etapempttmodel')

        # Deleting field 'SettingsEtapeFoad.vu_etape_inf'
        db.delete_column(u'foad_settingsetapefoad', 'vu_etape_inf')


    models = {
        u'django_apogee.etape': {
            'Meta': {'object_name': 'Etape', 'db_table': "u'ETAPE'"},
            'cod_cur': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_CUR'"}),
            'cod_cyc': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_CYC'"}),
            'cod_etp': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'COD_ETP'"}),
            'lib_etp': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'db_column': "u'LIB_ETP'"})
        },
        u'foad.comptemail': {
            'Meta': {'object_name': 'CompteMail', 'db_table': "'vpopmail'", 'managed': 'False'},
            'pw_name': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'primary_key': 'True'})
        },
        u'foad.etapempttmodel': {
            'Meta': {'object_name': 'EtapeMpttModel'},
            'etape': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['foad.SettingsEtapeFoad']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['foad.EtapeMpttModel']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'foad.foadcour': {
            'Meta': {'object_name': 'FoadCour', 'db_table': "'cl_cours'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'cours_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'cours_id'"}),
            'dbName': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'directory': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'enrollment_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'faculte': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'fake_code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'intitule': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'languageCourse': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'visible': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'foad.foadcouruser': {
            'Meta': {'object_name': 'FoadCourUser', 'db_table': "'cl_cours_user'"},
            'code_cours': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True', 'db_column': "'code_cours'"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'statut': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'team': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tutor': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foad.FoadUser']", 'db_column': "'user_id'"})
        },
        u'foad.foaddip': {
            'Meta': {'object_name': 'FoadDip', 'db_table': "'cl_dip_user'"},
            'dip_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foad.FoadUser']", 'null': 'True', 'db_column': "'user_id'"})
        },
        u'foad.foaduser': {
            'Meta': {'object_name': 'FoadUser', 'db_table': "'cl_user'"},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ied_code': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'official_code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'db_column': "'officialCode'"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'perso_email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'phoneNumber': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'statut': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'})
        },
        u'foad.settingsetapefoad': {
            'Meta': {'object_name': 'SettingsEtapeFoad', '_ormbases': [u'django_apogee.Etape']},
            'date_fermeture': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_ouverture': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'etape_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['django_apogee.Etape']", 'unique': 'True', 'primary_key': 'True'}),
            'vu_etape_inf': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['foad']