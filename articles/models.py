import urllib
import xml.etree.ElementTree as ET

from django.db import models
#from django.core.files.storage import FileSystemStorage

from info.models import Brother
#from ThetaTauMiami import settings


class Picture(models.Model):
#    image       = models.ImageField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to="articles/pictures/")
    image       = models.URLField()
    alt_text    = models.CharField(max_length=200, blank=True)
    subtitle    = models.CharField(max_length=500, blank=True)
    title       = models.CharField(max_length=250, blank=True)
    date        = models.DateField(null=True)
    
    def __unicode__(self):
        return str(self.date) + " " + self.title
    
    def __str__(self):
        return self.__unicode__()
    
class Gallery(models.Model):
    name = models.CharField(max_length=100)
    pictures = models.ManyToManyField(Picture, null=True)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class ArticleCategory(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class Article(models.Model):
    title           = models.CharField(max_length=200)
    author          = models.ForeignKey(Brother)
    date            = models.DateField()
#    article_xml     = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT),upload_to="articles/xml/")
    article_xml     = models.URLField()
    default_picture = models.ForeignKey(Picture)
    gallery         = models.ForeignKey(Gallery)
    category        = models.ForeignKey(ArticleCategory)
    
    def __unicode__(self):
        return str(self.date) + " " + str(self.author) + ": " + self.title
    
    def __str__(self):
        return self.__unicode__()
    
class ArticleEntity():
    def __init__(self, article):
        self.article = article
        self.subtitle = ''
        self.paras = []
        article_x = urllib.urlopen(self.article.article_xml)
        x = ''
        for lines in article_x.readlines():
            x += lines
        tree = ET.fromstring(x)
        self.subtitle = tree[1].text
        for para in tree[2]:
            self.paras.append( para.text.replace('\\n', '') )
        