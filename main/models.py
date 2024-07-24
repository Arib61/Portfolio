from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Service(models.Model): 
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name

class TechnicalSkill(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=500)  # Augmenter la taille maximale à 500 caractères

    def __str__(self):
        return self.name

class SoftSkill(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=500)  # Augmenter la taille maximale à 500 caractères

    def __str__(self):
        return self.name
    
class Certificate(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name

class ProjetML(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    outil_utilise = models.CharField(max_length=1000)
    algorithmes_utilises = models.TextField()
    lien_projet = models.URLField()
    lien_github = models.URLField()
    pdf = models.FileField(upload_to='mlpdf/', null=True, blank=True)

    def __str__(self):
        return self.titre


class ProjetDL(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    outil_utilise = models.CharField(max_length=1000)
    algorithmes_utilises = models.TextField()
    lien_projet = models.URLField()
    lien_github = models.URLField()
    pdf = models.FileField(upload_to='dlpdf/', null=True, blank=True)

    def __str__(self):
        return self.titre

class ProjetDEV(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    outil_utilise = models.CharField(max_length=1000)
    lien_projet = models.URLField()
    lien_github = models.URLField()
    

    def __str__(self):
        return self.titre