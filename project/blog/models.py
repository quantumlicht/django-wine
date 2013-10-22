from django.db import models
from corewine.models import Timestamp, Orderable

class BlogEntry(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('publication date')

    def __unicode__(self):
        return '(%s): %s' % (self.author, self.title)


class Comment(models.Model):
    blogEntry = models.ForeignKey(BlogEntry)
    author = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('publication date')

    def __unicode__(self):
        return self.author + ' ' + self.content[10:] + '...'
