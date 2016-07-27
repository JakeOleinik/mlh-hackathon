from django.db import models

class Article(models.Model):
    publicationID = models.IntegerField(default=0,blank=True, null=True)
    contentPackageID = models.IntegerField(default=0, blank=True, null=True)
    pageID = models.IntegerField(default=0)
    articleID = models.IntegerField(default=0)
    category = models.CharField(max_length=128, blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    author = models.CharField(max_length=128, blank=True, null=True)
    articleText = models.TextField(name='articleText', blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    hasImage = models.NullBooleanField(default=False, null=True)
    introduction = models.TextField(name='introduction', blank=True, null=True)
    publicationName = models.CharField(max_length=128, blank=True, null=True)
    publicationDate = models.DateTimeField(blank=True, null=True)
    words_only = models.TextField(name='words_only', null=True)
    built_dict = models.TextField(null=True)

    def __str__(self):
        return u'Article #{}, "{}" by {}'.format(self.articleID, self.title, self.author)

    def __unicode__(self):
        return u'Article #{}, "{}" by {}'.format(self.articleID, self.title, self.author)
