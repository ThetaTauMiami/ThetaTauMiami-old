from django.db import models

class Picture(models.Model):
    pic     = models.URLField()
    name    = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.__unicode__()