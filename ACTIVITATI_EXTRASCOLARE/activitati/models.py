from django.db import models

class Activitate(models.Model):
    titlu = models.CharField(max_length=200)
    descriere = models.TextField()
    data = models.DateField()
    categorie = models.CharField(max_length=100)
    imagine = models.ImageField(upload_to='activitati/', blank=True)
    coordonator = models.CharField(max_length=200, blank=True, null=True) # New field for coordinating teacher

    def __str__(self):
        return self.titlu

