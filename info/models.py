from django.db import models

# Create your models here.
class PledgeClass(models.Model):
    year        = models.CharField(max_length=4)
    semester    = models.CharField(max_length=10)
    bidOffer    = models.DateField()
    initiation  = models.DateField()
    name        = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.year + " " + self.semester
    
    def __str__(self):
        return self.__unicode__()
    
class Brother(models.Model):
    firstName       = models.CharField(max_length=50)
    middleName      = models.CharField(max_length=50)
    lastName        = models.CharField(max_length=50)
    pledgeClass     = models.ForeignKey(PledgeClass)
    uniqueId        = models.CharField(max_length=10)
    graduationYear  = models.CharField(max_length=4)
    isAlumni        = models.BooleanField()
    isPledge        = models.BooleanField()
    phone           = models.CharField(max_length=15)
    picture         = models.URLField()
    resume          = models.URLField()
    address         = models.CharField(max_length=200)
    bio             = models.CharField(max_length=500)
    
    def __unicode__(self):
        return str(self.pledgeClass) + " - " + self.lastName + ", " + self.firstName + " " + self.middleName
    
    def __str__(self):
        return self.__unicode__()
     
class Alumni(models.Model):
    brother             = models.ForeignKey(Brother)
    currentJob          = models.CharField(max_length=100)
    currentCompany      = models.CharField(max_length=150)
    jobOnGraduation     = models.CharField(max_length=100)
    companyOnGraduation = models.CharField(max_length=150)
    email               = models.EmailField()
    
    def __unicode__(self):
        return str(self.brother)
    
    def __str__(self):
        return self.__unicode__()
     
class Department(models.Model):
    abbrev  = models.CharField(max_length=3)
    name    = models.CharField(max_length=150)
    def __unicode__(self):
        return self.abbrev
    
    def __str__(self):
        return self.__unicode__()
       
class Major(models.Model):
    department  = models.ForeignKey(Department)
    majorName   = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.majorName
    
    def __str__(self):
        return self.__unicode__()

class HasMajor(models.Model):
    brother = models.ForeignKey(Brother)
    major   = models.ForeignKey(Major)
    
    def __unicode__(self):
        return str(self.brother) + " - " + str(self.major)
    
    def __str__(self):
        return self.__unicode__()
    
class Officer(models.Model):
    brother  = models.ForeignKey(Brother)
    position = models.CharField(max_length=50)
    ordering = models.IntegerField() # Represents the order it appears on the page - ties have no guarantee on how they will be ordered
    overview = models.CharField(max_length=500)
    
    def __unicode__(self):
        return self.position
    
    def __str__(self):
        return self.__unicode__()
    
    
class BrotherEntity():
    def __init__(self, brotherObj):
        self.brother = brotherObj
        hasMajors = HasMajor.objects.filter(brother = self.brother)
        self.majors = []
        for hasMajor in hasMajors:
            self.majors.append(hasMajor.major)
        
        