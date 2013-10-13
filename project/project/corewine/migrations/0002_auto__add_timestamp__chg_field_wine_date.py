# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Timestamp'
        db.create_table(u'corewine_timestamp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'corewine', ['Timestamp'])


        # Changing field 'Wine.date'
        db.alter_column(u'corewine_wine', 'date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):
        # Deleting model 'Timestamp'
        db.delete_table(u'corewine_timestamp')


        # Changing field 'Wine.date'
        db.alter_column(u'corewine_wine', 'date', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'corewine.acidity': {
            'Meta': {'object_name': 'Acidity'},
            'acidity': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Pending'", 'max_length': '60'}),
            'wineType': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'corewine.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Pending'", 'max_length': '60'}),
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
        u'corewine.timestamp': {
            'Meta': {'object_name': 'Timestamp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'corewine.wine': {
            'Meta': {'object_name': 'Wine'},
            'acidity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Acidity']"}),
            'alcool': ('django.db.models.fields.FloatField', [], {}),
            'appelation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'aroma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Aroma']"}),
            'cepage': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['corewine.Cepage']", 'symmetrical': 'False'}),
            'code_saq': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mouth_intensity': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'nose_intensity': ('django.db.models.fields.IntegerField', [], {}),
            'persistance': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'producer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rating': ('django.db.models.fields.FloatField', [], {}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['corewine.Tag']", 'symmetrical': 'False'}),
            'tanin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Tanin']"}),
            'taste': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Taste']"}),
            'teint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Teint']"}),
            'wineType': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['corewine']