# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ScheduledShow.active'
        db.add_column('schedule_scheduledshow', 'active', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ScheduledShow.active'
        db.delete_column('schedule_scheduledshow', 'active')


    models = {
        'schedule.scheduledshow': {
            'Meta': {'ordering': "['date', 'time']", 'object_name': 'ScheduledShow'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shows.Show']"}),
            'time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(19, 30)'})
        },
        'shows.show': {
            'Meta': {'ordering': "['name']", 'object_name': 'Show'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['schedule']
