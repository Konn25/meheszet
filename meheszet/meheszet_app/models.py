from django.db import models

natureOfBeekeeping = [(1, 'Álló'), (2, 'Vándor')]


# Create your models here.
class AddUser(models.Model):
    firstname = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=150, null=False, blank=False)
    beekepingNature = models.IntegerField(
        null=False,
        blank=False,
        choices=natureOfBeekeeping,
        default=1

    )
    smallProducerRegNumber = models.CharField(max_length=7, null=False, blank=False)

    def __str__(self):
        return self.username
