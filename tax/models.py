from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField( max_length=12, verbose_name="Telefono")
    name = models.CharField(max_length=100, verbose_name="Nombres")
    lastname = models.CharField(max_length=100, verbose_name="Apellidos")
    email = models.EmailField(max_length=30, verbose_name="Email")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "ususario"
        verbose_name_plural = "usuarios"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Ruc(models.Model):
    ruc = models.CharField(max_length=11, verbose_name="RUC")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "RUC"
        ordering = ['-created']

    def __str__(self):
        return self.ruc

class Contributor(models.Model):
    contperfil = models.ForeignKey(Profile, verbose_name="Usuario", related_name="get_contusers", on_delete=models.CASCADE)
    rucuser =  models.OneToOneField(Ruc, verbose_name="RUC", on_delete=models.CASCADE, related_name='get_contruc',)
    description = RichTextField(verbose_name="Descripción del negocio")
    facebook = models.URLField(verbose_name="URL Facebook",max_length = 200, blank=True)
    website = models.URLField(verbose_name="Sitio web",max_length = 200, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "contribuidor"
        verbose_name_plural = "contribuidores"
        ordering = ['-created']

    def __str__(self):
        return self.rucuser

class Ficharuc(models.Model):
    rucuser = models.OneToOneField(Ruc, verbose_name="RUC", on_delete=models.CASCADE, related_name='get_ficharuc',)
    state = models.CharField(max_length=30, verbose_name="Estado")
    condition = models.CharField(max_length=20, verbose_name="Condicion")
    contributor_type = models.CharField(max_length=30, verbose_name="Tipo de contribuidor")
    business_name = models.CharField(max_length=100, verbose_name="Nombre del negocio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Ficha RUC"
        verbose_name_plural = "Fichas RUCs"
        ordering = ['-created']

    def __str__(self):
        return self.rucuser

class Schedule(models.Model):
    year = models.DateField(null=True, blank=True)
    month = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    class Meta:
        verbose_name = "Calendario"
        verbose_name_plural = "Calendarios"

class Tax(models.Model):
    taxperfil = models.ForeignKey(Profile, verbose_name="Usuario", related_name="get_taxusers", on_delete=models.CASCADE)
    contribuidor = models.ForeignKey(Contributor, verbose_name="Contribuidor", related_name="get_contributors", on_delete=models.CASCADE)
    buy = models.CharField(max_length=6, verbose_name="Compra")
    sales = models.CharField(max_length=6, verbose_name="Ventas")
    fees = models.CharField(max_length=4, verbose_name="Tarifa")
    perceptions = models.CharField(max_length=6, verbose_name="Percepciones")
    pay = models.CharField(max_length=4, verbose_name="Pagar")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "impuesto"
        verbose_name_plural = "impuestos"
        ordering = ['-created']

    def __str__(self):
        return self.taxperfil