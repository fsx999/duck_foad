# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AuditeurLibreApogee'
        db.create_table(u'foad_auditeurlibreapogee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('personal_email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(default=None, max_length=15, null=True)),
            ('code_ied', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('status_modified', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('access_claroline', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_registration_current_year', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('annee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_apogee.AnneeUni'])),
        ))
        db.send_create_signal(u'foad', ['AuditeurLibreApogee'])


    def backwards(self, orm):
        # Deleting model 'AuditeurLibreApogee'
        db.delete_table(u'foad_auditeurlibreapogee')


    models = {
        u'django_apogee.anneeuni': {
            'Meta': {'ordering': "[u'-cod_anu']", 'object_name': 'AnneeUni', 'db_table': "u'ANNEE_UNI'"},
            'cod_anu': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True', 'db_column': "u'COD_ANU'"}),
            'eta_anu_iae': ('django.db.models.fields.CharField', [], {'default': "u'I'", 'max_length': '1', 'db_column': "u'ETA_ANU_IAE'"})
        },
        u'django_apogee.etape': {
            'Meta': {'object_name': 'Etape', 'db_table': "u'ETAPE'"},
            'cod_cur': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_CUR'"}),
            'cod_cyc': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_CYC'"}),
            'cod_etp': ('django.db.models.fields.CharField', [], {'max_length': '6', 'primary_key': 'True', 'db_column': "u'COD_ETP'"}),
            'lib_etp': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'db_column': "u'LIB_ETP'"})
        },
        u'django_apogee.individu': {
            'Meta': {'object_name': 'Individu', 'db_table': "u'INDIVIDU'"},
            'cod_cle_nne_ind': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_CLE_NNE_IND'"}),
            'cod_etb': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'db_column': "u'COD_ETB'"}),
            'cod_etu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'COD_ETU'"}),
            'cod_fam': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_FAM'"}),
            'cod_ind': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'COD_IND'"}),
            'cod_ind_opi': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'COD_IND_OPI'"}),
            'cod_nne_ind': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'db_column': "u'COD_NNE_IND'"}),
            'cod_pay_nat': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_PAY_NAT'"}),
            'cod_sex_etu': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_SEX_ETU'"}),
            'cod_sim': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'COD_SIM'"}),
            'cod_thp': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_THP'"}),
            'cod_uti': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'db_column': "u'COD_UTI'"}),
            'daa_ens_sup': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'DAA_ENS_SUP'"}),
            'daa_ent_etb': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'DAA_ENT_ETB'"}),
            'daa_etb': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'DAA_ETB'"}),
            'daa_lbt_ind': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'db_column': "u'DAA_LBT_IND'"}),
            'dat_cre_ind': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DAT_CRE_IND'"}),
            'dat_mod_ind': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DAT_MOD_IND'"}),
            'date_nai_ind': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DATE_NAI_IND'"}),
            'dmm_lbt_ind': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'DMM_LBT_IND'"}),
            'lib_nom_pat_ind': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'db_column': "u'LIB_NOM_PAT_IND'"}),
            'lib_nom_usu_ind': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'db_column': "u'LIB_NOM_USU_IND'"}),
            'lib_pr1_ind': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'db_column': "u'LIB_PR1_IND'"}),
            'lib_pr2_ind': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'db_column': "u'LIB_PR2_IND'"}),
            'lib_pr3_ind': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'db_column': "u'LIB_PR3_IND'"}),
            'tem_date_nai_rel': ('django.db.models.fields.CharField', [], {'default': "u'O'", 'max_length': '1', 'null': 'True', 'db_column': "u'TEM_DATE_NAI_REL'"})
        },
        u'django_apogee.insadmetp': {
            'Meta': {'object_name': 'InsAdmEtp', 'db_table': "u'INS_ADM_ETP_COPY'"},
            'cod_anu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.AnneeUni']"}),
            'cod_cge': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_CGE'"}),
            'cod_dip': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'db_column': "u'COD_DIP'"}),
            'cod_etp': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'db_column': "u'COD_ETP'"}),
            'cod_ind': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'etapes_ied'", 'db_column': "u'COD_IND'", 'to': u"orm['django_apogee.Individu']"}),
            'cod_pru': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'COD_PRU'"}),
            'cod_vrs_vdi': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'db_column': "u'COD_VRS_VDI'"}),
            'cod_vrs_vet': ('django.db.models.fields.CharField', [], {'max_length': '3', 'db_column': "u'COD_VRS_VET'"}),
            'dat_annul_res_iae': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DAT_ANNUL_RES_IAE'"}),
            'dat_cre_iae': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DAT_CRE_IAE'"}),
            'dat_mod_iae': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'DAT_MOD_IAE'"}),
            'eta_iae': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'ETA_IAE'"}),
            'eta_pmt_iae': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'ETA_PMT_IAE'"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'nbr_ins_cyc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NBR_INS_CYC'"}),
            'nbr_ins_dip': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NBR_INS_DIP'"}),
            'nbr_ins_etp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NBR_INS_ETP'"}),
            'num_occ_iae': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'db_column': "u'NUM_OCC_IAE'"}),
            'tem_iae_prm': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'db_column': "u'TEM_IAE_PRM'"})
        },
        u'foad.auditeurlibreapogee': {
            'Meta': {'object_name': 'AuditeurLibreApogee'},
            'access_claroline': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'annee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_apogee.AnneeUni']"}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'code_ied': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'date_registration_current_year': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'personal_email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '15', 'null': 'True'}),
            'status_modified': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'foad.comptemail': {
            'Meta': {'object_name': 'CompteMail', 'db_table': "'vpopmail'", 'managed': 'False'},
            'pw_name': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'primary_key': 'True'})
        },
        u'foad.etapempttmodel': {
            'Meta': {'object_name': 'EtapeMpttModel'},
            'etape': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'mptt'", 'unique': 'True', 'to': u"orm['foad.SettingsEtapeFoad']"}),
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
        u'foad.remontee': {
            'Meta': {'object_name': 'Remontee'},
            'etape': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'remontee'", 'unique': 'True', 'to': u"orm['django_apogee.InsAdmEtp']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_plateforme': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'remontee': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'foad.settingsanneefoad': {
            'Meta': {'ordering': "[u'-cod_anu']", 'object_name': 'SettingsAnneeFoad', '_ormbases': [u'django_apogee.AnneeUni']},
            'annee_en_cour': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'anneeuni_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['django_apogee.AnneeUni']", 'unique': 'True', 'primary_key': 'True'}),
            'inscription': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'foad.settingsetapefoad': {
            'Meta': {'object_name': 'SettingsEtapeFoad', '_ormbases': [u'django_apogee.Etape']},
            'c2i': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_fermeture': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_ouverture': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'etape_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['django_apogee.Etape']", 'unique': 'True', 'primary_key': 'True'}),
            'vu_etape_inf': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['foad']