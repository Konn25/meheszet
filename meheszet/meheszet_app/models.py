from django.db import models

# Create your models here.
class AddUser(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.username+" "+self.email



class Breeding(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False, blank=False)
    breedingcode = models.CharField(max_length=7, null=False, blank=False)

    def __str__(self):
        return self.username+" | "+self.breedingcode

class Beehive(models.Model):
    COLOR_CHOICES = (
         ('Kérlek válassz szint','NULL'),
         ('Kék','Kék'),
         ('Fehér','Fehér'),
         ('Piros','Piros'),
         ('Sárga','Sárga'),
         ('Zöld','Zöld'),
    )

    BEEHIVE_STRENGTH = (
        ('Kérlek válassz erősséget','NULL'),
        ('Gyenge', 'Gyenge'),
        ('Átlagos','Átlagos'),
        ('Erős','Erős')
    )

    TYPE_OF_HIVE = (
        ('NULL','Kérlek válassz'),
        ('Langstroth','Langstroth'),
        ('Warre','Warre'),
        ('Neiszer','Neiszer-féle ikerkaptár'),
        ('Kis Boczonádi','Kis Boczonádi'),
        ('Balogh Bálint féle','Balogh Bálint-féle kaptár'),
        ('Mogor','Mogor'),
        ('Hunor','Hunor'),
        ('Közép Boczonádi','Közép Boczonádi'),
        ('Dadant-Blatt féle','Dadant-Blatt féle kaptár'),
        ('Zander','Zander féle'),
        ('Ignácz-féle','Ignácz-féle Kaptár'),
        ('Debreceni','Debreceni kaptár'),
        ('Nagy Boczonádi','Nagy Boczonádi')
    )
    id = models.AutoField(primary_key=True)
    breedingcode = models.CharField(max_length=7, null=False, blank=False)
    beehivenumber = models.CharField(max_length=4, null=False, blank=False)
    quenbeecolor = models.CharField(choices=COLOR_CHOICES,max_length=20)
    quenbeeyear = models.CharField(max_length=4,null=False, blank=False)
    beehivestrength = models.CharField(choices=BEEHIVE_STRENGTH,max_length=24)
    typeofhive = models.CharField(choices=TYPE_OF_HIVE,max_length=25)

    def __str__(self):
        return "BreedingCode: "+self.breedingcode+" |  BeehiveNumber: "+self.beehivenumber+"| Type of hive: "+self.typeofhive

