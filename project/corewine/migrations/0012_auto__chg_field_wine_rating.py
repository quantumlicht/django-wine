# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Wine.rating'
        db.alter_column(u'corewine_wine', 'rating', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1))

    def backwards(self, orm):

        # Changing field 'Wine.rating'
        db.alter_column(u'corewine_wine', 'rating', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1))

    models = {
        u'corewine.acidity': {
            'Meta': {'ordering': "['order']", 'object_name': 'Acidity'},
            'acidity': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'acidity_en': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'acidity_fr': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'corewine.appelation': {
            'Meta': {'ordering': "['appelation']", 'object_name': 'Appelation'},
            'appelation': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'blank': 'True'}),
            'appelation_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'appelation_fr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'})
        },
        u'corewine.aroma': {
            'Meta': {'ordering': "['order']", 'object_name': 'Aroma'},
            'aroma': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'aroma_en': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'aroma_fr': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'corewine.cepage': {
            'Meta': {'ordering': "['cepage']", 'object_name': 'Cepage'},
            'cepage': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'}),
            'wineType': ('django.db.models.fields.CharField', [], {'default': "'White'", 'max_length': '60'})
        },
        u'corewine.country': {
            'Meta': {'ordering': "['country']", 'object_name': 'Country'},
            'country': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'country_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'country_fr': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'})
        },
        u'corewine.producer': {
            'Meta': {'ordering': "['producer']", 'object_name': 'Producer'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'producer': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'})
        },
        u'corewine.region': {
            'Meta': {'ordering': "['region']", 'object_name': 'Region'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'region_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'region_fr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'})
        },
        u'corewine.tag': {
            'Meta': {'ordering': "['tag']", 'object_name': 'Tag'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'tag_en': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'tag_fr': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'wineType': ('django.db.models.fields.CharField', [], {'default': "'White'", 'max_length': '60'})
        },
        u'corewine.tanin': {
            'Meta': {'ordering': "['order']", 'object_name': 'Tanin'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'tanin': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'tanin_en': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'tanin_fr': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'corewine.taste': {
            'Meta': {'ordering': "['order']", 'object_name': 'Taste'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'taste': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'taste_en': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'taste_fr': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'corewine.teint': {
            'Meta': {'object_name': 'Teint'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'teint': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'teint_en': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'teint_fr': ('django.db.models.fields.CharField', [], {'max_length': '60', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'wineType': ('django.db.models.fields.CharField', [], {'default': "'White'", 'max_length': '60'})
        },
        u'corewine.wine': {
            'Meta': {'ordering': "['name']", 'object_name': 'Wine'},
            'acidity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Acidity']"}),
            'alcool': ('django.db.models.fields.FloatField', [], {}),
            'appelation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Appelation']", 'null': 'True', 'blank': 'True'}),
            'aroma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Aroma']"}),
            'cepage': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['corewine.Cepage']", 'symmetrical': 'False'}),
            'code_saq': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'mouth_intensity': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'nose_intensity': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'persistance': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'producer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Producer']"}),
            'rating': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Region']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['corewine.Tag']", 'null': 'True', 'blank': 'True'}),
            'tanin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Tanin']", 'blank': 'True'}),
            'taste': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Taste']"}),
            'teint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Teint']"}),
            'wineType': ('django.db.models.fields.CharField', [], {'default': "'White'", 'max_length': '60'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['corewine']