from django.db import models
from info.models import Brother


class Picture(models.Model):
    image = models.ImageField(upload_to="articles/pictures/")
    alt_text = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500)
    title = models.CharField(max_length=250)
    date = models.DateField()
    def __unicode__(self):
        return str(self.date) + " " + self.title
    
class Gallery(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
class InGallery(models.Model):
    image = models.ForeignKey(Picture)
    gallery = models.ForeignKey(Gallery)
    
    def __unicode__(self):
        return str(self.gallery) + " - " + str(self.image)
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Brother)
    date = models.DateField()
    article_xml = models.FileField(upload_to="articles/xml/")
    default_picture = models.ForeignKey(Picture)
    gallery = models.ForeignKey(Gallery)

    def __unicode__(self):
        return str(self.date) + " " + str(self.author) + ": " + self.title