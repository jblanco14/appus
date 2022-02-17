from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClaseModelo(models.Model):

    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now_add=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True,null=True)

   
   # Para que no lo tenga en cuenta en una migracion pero si hereda.

    class Meta:
        abstract=True