from django.db import models

from bases.models import ClaseModelo

# Create your models here.
class TipoDocumento(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Tipo de Documento',
        unique=True 
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(TipoDocumento, self).save()

    class Meta:
        verbose_name_plural = "Documentos"

class SocialSec(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='SocialSec',
        unique=True 
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SocialSec, self).save()

    class Meta:
        verbose_name_plural = "Socials"

class Eps(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Eps',
        unique=True 
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Eps, self).save()

    class Meta:
        verbose_name_plural = "Eps"

class EstadoCivil(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='EstadoCivil',
        unique=True 
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(EstadoCivil, self).save()

    class Meta:
        verbose_name_plural = "Estado Civil"


class Sexo(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Sexo',
        unique=True 
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Sexo, self).save()

    class Meta:
        verbose_name_plural = "Sexo"

class Ciudad(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Ciudades y estados',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Ciudad, self).save()

    class Meta:
        verbose_name_plural = "Ciudades y estados"

class Profesion(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Tipo de profesion',
        unique=True 
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Profesion, self).save()

    class Meta:
        verbose_name_plural = "Profesion"

class Nacionalidad(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Seleccione Nacionalidad',
        unique=True 
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Nacionalidad, self).save()

    class Meta:
        verbose_name_plural = "Nacionalidad"


class Empleado(ClaseModelo):

    numero_identificacion = models.CharField(
        max_length=30,
        help_text='Numero de identificación',
        unique=True 
    )
  
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    lugar_nacimiento = models.CharField(max_length=30)
    direccion_residencia = models.CharField(max_length=50)
    barrio = models.CharField(max_length=50)
    numero_telefonico = models.CharField(max_length=15)
    correo_electronico = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)
    contacto_emergencia = models.CharField(max_length=30)
    numero_telefonico2 = models.CharField(max_length=15)
    

    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    ciudad_resident = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    social_security = models.ForeignKey(SocialSec, on_delete=models.CASCADE)
    eps = models.ForeignKey(Eps, on_delete=models.CASCADE)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE) 

    def __str__(self):
        return '{}'.format(self.numero_identificacion)
    
    def save(self):
        self.numero_identificacion = self.numero_identificacion.upper()
        super(Empleado,self).save()
    
    class Meta:
        verbose_name_plural = "Empleados"
        unique_together = ('numero_identificacion','apellidos')
        
 

