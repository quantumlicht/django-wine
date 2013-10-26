# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        # db.create_table(u'corewine_region', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('status', self.gf('django.db.models.fields.CharField')(default='p', max_length=60)),
        #     ('region', self.gf('django.db.models.fields.CharField')(max_length=100)),
        # ))
        db.send_create_signal(u'corewine', ['Region'])

        # Adding model 'Appelation'
        # db.create_table(u'corewine_appelation', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('status', self.gf('django.db.models.fields.CharField')(default='p', max_length=60)),
        #     ('appelation', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        # ))
        db.send_create_signal(u'corewine', ['Appelation'])

        # Adding model 'Producer'
        # db.create_table(u'corewine_producer', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('status', self.gf('django.db.models.fields.CharField')(default='p', max_length=60)),
        #     ('producer', self.gf('django.db.models.fields.CharField')(max_length=100)),
        # ))
        db.send_create_signal(u'corewine', ['Producer'])


        # Renaming column for 'Wine.appelation' to match new field type.
        db.rename_column(u'corewine_wine', 'appelation', 'appelation_id')
        # Changing field 'Wine.appelation'
        db.alter_column(u'corewine_wine', 'appelation_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['corewine.Appelation']))
        # Adding index on 'Wine', fields ['appelation']
        db.create_index(u'corewine_wine', ['appelation_id'])


        # Renaming column for 'Wine.producer' to match new field type.
        db.rename_column(u'corewine_wine', 'producer', 'producer_id')
        # Changing field 'Wine.producer'
        db.alter_column(u'corewine_wine', 'producer_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['corewine.Producer']))
        # Adding index on 'Wine', fields ['producer']
        db.create_index(u'corewine_wine', ['producer_id'])


        # Renaming column for 'Wine.region' to match new field type.
        db.rename_column(u'corewine_wine', 'region', 'region_id')
        # Changing field 'Wine.region'
        db.alter_column(u'corewine_wine', 'region_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['corewine.Region']))
        # Adding index on 'Wine', fields ['region']
        # db.create_index(u'corewine_wine', ['region_id'])


    def backwards(self, orm):
        # Removing index on 'Wine', fields ['region']
        db.delete_index(u'corewine_wine', ['region_id'])

        # Removing index on 'Wine', fields ['producer']
        db.delete_index(u'corewine_wine', ['producer_id'])

        # Removing index on 'Wine', fields ['appelation']
        db.delete_index(u'corewine_wine', ['appelation_id'])

        # Deleting model 'Region'
        db.delete_table(u'corewine_region')

        # Deleting model 'Appelation'
        db.delete_table(u'corewine_appelation')

        # Deleting model 'Producer'
        db.delete_table(u'corewine_producer')


        # Renaming column for 'Wine.appelation' to match new field type.
        db.rename_column(u'corewine_wine', 'appelation_id', 'appelation')
        # Changing field 'Wine.appelation'
        db.alter_column(u'corewine_wine', 'appelation', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Renaming column for 'Wine.producer' to match new field type.
        db.rename_column(u'corewine_wine', 'producer_id', 'producer')
        # Changing field 'Wine.producer'
        db.alter_column(u'corewine_wine', 'producer', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Renaming column for 'Wine.region' to match new field type.
        db.rename_column(u'corewine_wine', 'region_id', 'region')
        # Changing field 'Wine.region'
        db.alter_column(u'corewine_wine', 'region', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'corewine.acidity': {
            'Meta': {'object_name': 'Acidity'},
            'acidity': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'corewine.appelation': {
            'Meta': {'object_name': 'Appelation'},
            'appelation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'})
        },
        u'corewine.aroma': {
            'Meta': {'object_name': 'Aroma'},
            'aroma': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'corewine.cepage': {
            'Meta': {'object_name': 'Cepage'},
            'cepage': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'}),
            'wineType': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'corewine.country': {
            'Meta': {'object_name': 'Country'},
            'country': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'country_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'country_fr': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'})
        },
        u'corewine.producer': {
            'Meta': {'object_name': 'Producer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'})
        },
        u'corewine.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'})
        },
        u'corewine.tag': {
            'Meta': {'object_name': 'Tag'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'wineType': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'corewine.tanin': {
            'Meta': {'object_name': 'Tanin'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'tanin': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        u'corewine.taste': {
            'Meta': {'object_name': 'Taste'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'taste': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        u'corewine.teint': {
            'Meta': {'object_name': 'Teint'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'teint': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'wineType': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'corewine.wine': {
            'Meta': {'object_name': 'Wine'},
            'acidity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Acidity']"}),
            'alcool': ('django.db.models.fields.FloatField', [], {}),
            'appelation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Appelation']"}),
            'aroma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Aroma']"}),
            'cepage': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['corewine.Cepage']", 'symmetrical': 'False'}),
            'code_saq': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'mouth_intensity': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'nose_intensity': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'persistance': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'producer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Producer']"}),
            'rating': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Region']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['corewine.Tag']", 'null': 'True', 'blank': 'True'}),
            'tanin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Tanin']", 'blank': 'True'}),
            'taste': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Taste']"}),
            'teint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Teint']"}),
            'wineType': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['corewine']