from django.db import models
from info.models import Brother
from ThetaTauMiami import settings

from django.core.files.storage import FileSystemStorage

class Picture(models.Model):
#    image       = models.ImageField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to="articles/pictures/")
    image       = models.URLField()
    alt_text    = models.CharField(max_length=200)
    subtitle    = models.CharField(max_length=500)
    title       = models.CharField(max_length=250)
    date        = models.DateField()
    
    def __unicode__(self):
        return str(self.date) + " " + self.title
    
    def __str__(self):
        return self.__unicode__()
    
class Gallery(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class InGallery(models.Model):
    image   = models.ForeignKey(Picture)
    gallery = models.ForeignKey(Gallery)
    
    def __unicode__(self):
        return str(self.gallery) + " - " + str(self.image)
    
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