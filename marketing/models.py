from django.db import models
from ThetaTauMiami import settings

from django.core.files.storage import FileSystemStorage

class Picture(models.Model):
#    pic     = models.ImageField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to="marketing/pictures/")
    pic     = models.URLField()
    name    = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.__unicode__()