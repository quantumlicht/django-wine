# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Acidity'
        db.create_table(u'corewine_acidity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('acidity', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'corewine', ['Acidity'])

        # Adding model 'Aroma'
        db.create_table(u'corewine_aroma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('aroma', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'corewine', ['Aroma'])

        # Adding model 'Tanin'
        db.create_table(u'corewine_tanin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('tanin', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'corewine', ['Tanin'])

        # Adding model 'Teint'
        db.create_table(u'corewine_teint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('wineType', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('teint', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'corewine', ['Teint'])

        # Adding model 'Taste'
        db.create_table(u'corewine_taste', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('taste', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'corewine', ['Taste'])

        # Adding model 'Cepage'
        db.create_table(u'corewine_cepage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wineType', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('status', self.gf('django.db.models.fields.CharField')(default='Pending', max_length=60)),
            ('cepage', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'corewine', ['Cepage'])

        # Adding model 'Tag'
        db.create_table(u'corewine_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wineType', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('status', self.gf('django.db.models.fields.CharField')(default='Pending', max_length=60)),
            ('tag', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'corewine', ['Tag'])

        # Adding model 'Wine'
        db.create_table(u'corewine_wine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wineType', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('producer', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('appelation', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('alcool', self.gf('django.db.models.fields.FloatField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('code_saq', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('nose_intensity', self.gf('django.db.models.fields.IntegerField')()),
            ('mouth_intensity', self.gf('django.db.models.fields.IntegerField')()),
            ('persistance', self.gf('django.db.models.fields.IntegerField')()),
            ('rating', self.gf('django.db.models.fields.FloatField')()),
            ('teint', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['corewine.Teint'])),
            ('aroma', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['corewine.Aroma'])),
            ('taste', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['corewine.Taste'])),
            ('acidity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['corewine.Acidity'])),
            ('tanin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['corewine.Tanin'])),
        ))
        db.send_create_signal(u'corewine', ['Wine'])

        # Adding M2M table for field cepage on 'Wine'
        m2m_table_name = db.shorten_name(u'corewine_wine_cepage')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('wine', models.ForeignKey(orm[u'corewine.wine'], null=False)),
            ('cepage', models.ForeignKey(orm[u'corewine.cepage'], null=False))
        ))
        db.create_unique(m2m_table_name, ['wine_id', 'cepage_id'])

        # Adding M2M table for field tag on 'Wine'
        m2m_table_name = db.shorten_name(u'corewine_wine_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('wine', models.ForeignKey(orm[u'corewine.wine'], null=False)),
            ('tag', models.ForeignKey(orm[u'corewine.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['wine_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Acidity'
        db.delete_table(u'corewine_acidity')

        # Deleting model 'Aroma'
        db.delete_table(u'corewine_aroma')

        # Deleting model 'Tanin'
        db.delete_table(u'corewine_tanin')

        # Deleting model 'Teint'
        db.delete_table(u'corewine_teint')

        # Deleting model 'Taste'
        db.delete_table(u'corewine_taste')

        # Deleting model 'Cepage'
        db.delete_table(u'corewine_cepage')

        # Deleting model 'Tag'
        db.delete_table(u'corewine_tag')

        # Deleting model 'Wine'
        db.delete_table(u'corewine_wine')

        # Removing M2M table for field cepage on 'Wine'
        db.delete_table(db.shorten_name(u'corewine_wine_cepage'))

        # Removing M2M table for field tag on 'Wine'
        db.delete_table(db.shorten_name(u'corewine_wine_tag'))


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
        u'corewine.wine': {
            'Meta': {'object_name': 'Wine'},
            'acidity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Acidity']"}),
            'alcool': ('django.db.models.fields.FloatField', [], {}),
            'appelation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'aroma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Aroma']"}),
            'cepage': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['corewine.Cepage']", 'symmetrical': 'False'}),
            'code_saq': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
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