# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FoadUser'
        db.create_table('cl_user', (
            ('user_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('statut', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('ied_code', self.gf('django.db.models.fields.CharField')(max_length=8, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=60, null=True)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=60, null=True)),
            ('official_code', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, db_column='officialCode')),
            ('phoneNumber', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('perso_email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'foad', ['FoadUser'])

        # Adding model 'FoadDip'
        db.create_table('cl_dip_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foad.FoadUser'], null=True, db_column='user_id')),
            ('dip_id', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
        ))
        db.send_create_signal(u'foad', ['FoadDip'])

        # Adding model 'FoadCourUser'
        db.create_table('cl_cours_user', (
            ('code_cours', self.gf('django.db.models.fields.CharField')(max_length=40, primary_key=True, db_column='code_cours')),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foad.FoadUser'], db_column='user_id')),
            ('statut', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=60, null=True)),
            ('team', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tutor', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'foad', ['FoadCourUser'])

        # Adding model 'FoadCour'
        db.create_table('cl_cours', (
            ('cours_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column='cours_id')),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('fake_code', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('directory', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('dbName', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('languageCourse', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('faculte', self.gf('django.db.models.fields.CharField')(max_length=12, null=True)),
            ('intitule', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('visible', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('enrollment_key', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'foad', ['FoadCour'])


    def backwards(self, orm):
        # Deleting model 'FoadUser'
        db.delete_table('cl_user')

        # Deleting model 'FoadDip'
        db.delete_table('cl_dip_user')

        # Deleting model 'FoadCourUser'
        db.delete_table('cl_cours_user')

        # Deleting model 'FoadCour'
        db.delete_table('cl_cours')


    models = {
        u'foad.comptemail': {
            'Meta': {'object_name': 'CompteMail', 'db_table': "'vpopmail'", 'managed': 'False'},
            'pw_name': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'primary_key': 'True'})
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
        }
    }

    complete_apps = ['foad']