from django.db import models


class BlogEntry(models.Model):
    author = models.CharField(max_length=200)
    content = models.TextField()

    def __unicode__(self):
        return self.author + ' ' + self.content[10:] + '...'
