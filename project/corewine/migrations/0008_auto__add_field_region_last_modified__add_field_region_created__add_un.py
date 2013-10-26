# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Region.last_modified'
        db.add_column(u'corewine_region', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Region.created'
        db.add_column(u'corewine_region', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'Region', fields ['region']
        db.create_unique(u'corewine_region', ['region'])

        # Adding field 'Country.last_modified'
        db.add_column(u'corewine_country', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.created'
        db.add_column(u'corewine_country', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Appelation.last_modified'
        db.add_column(u'corewine_appelation', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Appelation.created'
        db.add_column(u'corewine_appelation', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'Appelation', fields ['appelation']
        db.create_unique(u'corewine_appelation', ['appelation'])

        # Adding field 'Taste.last_modified'
        db.add_column(u'corewine_taste', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Taste.created'
        db.add_column(u'corewine_taste', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Aroma.last_modified'
        db.add_column(u'corewine_aroma', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Aroma.created'
        db.add_column(u'corewine_aroma', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'Cepage', fields ['cepage']
        db.create_unique(u'corewine_cepage', ['cepage'])

        # Adding field 'Producer.last_modified'
        db.add_column(u'corewine_producer', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Producer.created'
        db.add_column(u'corewine_producer', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'Producer', fields ['producer']
        db.create_unique(u'corewine_producer', ['producer'])

        # Adding field 'Acidity.last_modified'
        db.add_column(u'corewine_acidity', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Acidity.created'
        db.add_column(u'corewine_acidity', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Teint.last_modified'
        db.add_column(u'corewine_teint', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Teint.created'
        db.add_column(u'corewine_teint', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Tanin.last_modified'
        db.add_column(u'corewine_tanin', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now=True, blank=True),
                      keep_default=False)

        # Adding field 'Tanin.created'
        db.add_column(u'corewine_tanin', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 26, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'Producer', fields ['producer']
        db.delete_unique(u'corewine_producer', ['producer'])

        # Removing unique constraint on 'Cepage', fields ['cepage']
        db.delete_unique(u'corewine_cepage', ['cepage'])

        # Removing unique constraint on 'Appelation', fields ['appelation']
        db.delete_unique(u'corewine_appelation', ['appelation'])

        # Removing unique constraint on 'Region', fields ['region']
        db.delete_unique(u'corewine_region', ['region'])

        # Deleting field 'Region.last_modified'
        db.delete_column(u'corewine_region', 'last_modified')

        # Deleting field 'Region.created'
        db.delete_column(u'corewine_region', 'created')

        # Deleting field 'Country.last_modified'
        db.delete_column(u'corewine_country', 'last_modified')

        # Deleting field 'Country.created'
        db.delete_column(u'corewine_country', 'created')

        # Deleting field 'Appelation.last_modified'
        db.delete_column(u'corewine_appelation', 'last_modified')

        # Deleting field 'Appelation.created'
        db.delete_column(u'corewine_appelation', 'created')

        # Deleting field 'Taste.last_modified'
        db.delete_column(u'corewine_taste', 'last_modified')

        # Deleting field 'Taste.created'
        db.delete_column(u'corewine_taste', 'created')

        # Deleting field 'Aroma.last_modified'
        db.delete_column(u'corewine_aroma', 'last_modified')

        # Deleting field 'Aroma.created'
        db.delete_column(u'corewine_aroma', 'created')

        # Deleting field 'Producer.last_modified'
        db.delete_column(u'corewine_producer', 'last_modified')

        # Deleting field 'Producer.created'
        db.delete_column(u'corewine_producer', 'created')

        # Deleting field 'Acidity.last_modified'
        db.delete_column(u'corewine_acidity', 'last_modified')

        # Deleting field 'Acidity.created'
        db.delete_column(u'corewine_acidity', 'created')

        # Deleting field 'Teint.last_modified'
        db.delete_column(u'corewine_teint', 'last_modified')

        # Deleting field 'Teint.created'
        db.delete_column(u'corewine_teint', 'created')

        # Deleting field 'Tanin.last_modified'
        db.delete_column(u'corewine_tanin', 'last_modified')

        # Deleting field 'Tanin.created'
        db.delete_column(u'corewine_tanin', 'created')


    models = {
        u'corewine.acidity': {
            'Meta': {'object_name': 'Acidity'},
            'acidity': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'corewine.appelation': {
            'Meta': {'object_name': 'Appelation'},
            'appelation': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'})
        },
        u'corewine.aroma': {
            'Meta': {'object_name': 'Aroma'},
            'aroma': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'corewine.cepage': {
            'Meta': {'object_name': 'Cepage'},
            'cepage': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
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
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'})
        },
        u'corewine.producer': {
            'Meta': {'object_name': 'Producer'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'producer': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'})
        },
        u'corewine.region': {
            'Meta': {'object_name': 'Region'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
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
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'tanin': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        u'corewine.taste': {
            'Meta': {'object_name': 'Taste'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'taste': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        u'corewine.teint': {
            'Meta': {'object_name': 'Teint'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 26, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
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