from django.db import models
from django.views.generic import ListView, CreateView, TemplateView, DeleteView, View
from mongoengine import Document,fields
from django import forms

# Create your models here.

class Inicio(models.Model):
    youtube = models.TextField(max_length=20000,null=True,blank=True)
    imagenInicio = models.ImageField(upload_to='static/img',blank=True)
    iframe1= models.TextField(max_length=20000,null=True,blank=True)
    iframe2= models.TextField(max_length=20000,null=True,blank=True)
    iframe3= models.TextField(max_length=20000,null=True,blank=True)
    iframe4= models.TextField(max_length=20000,null=True,blank=True)

class Asociacion(models.Model):
    textoAso = models.TextField(max_length=2000,null=True)
    centroF = models.ImageField(upload_to='static/img')
    textoAsociacion= models.TextField(max_length=2000,blank=True)
    fotop = models.ImageField(upload_to='static/img')
 
    
    def __str__(self):         
        return self.textoAso

class Proyecto(models.Model):
    titulo =models.CharField(max_length=200,null=True)
    textop=models.TextField(max_length=2000,blank=True)
  

    def __str__(self):         
        return self.titulo
    class Meta:
        ordering = ['titulo']



class DatosContacto(models.Model):
    direccion = models.CharField(max_length=100, null=True)
    tel = models.IntegerField(null= True,blank=True)
    horario = models.CharField(max_length=80, null=True)
    mail = models.EmailField(null= True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    facebook= models.URLField(null=True,blank=True)
    estatutos= models.TextField(max_length=10000, null=True)
    aviso= models.TextField(max_length=10000, null=True,blank=True)
    cookies= models.TextField(max_length=10000, null=True,blank=True)

    
    
    def __str__(self):         
        return self.direccion

    

class EntradaBlog(models.Model):
    titulo = models.CharField(max_length=70,blank=True)
    descripcion = models.TextField(null=True)
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to='static/img',blank=True)
    destacados = models.BooleanField(default=False,blank=True)


    def __str__(self):         
        return self.titulo


class Filosofia(models.Model):
    titulomision=models.CharField(max_length=70,null=True)
    mision = models.TextField(max_length=5000,null=True,blank=True)
    titulovision= models.CharField(max_length=70,null=True)
    vision = models.TextField(max_length=5000,null=True,blank=True)
    titulovalores=models.CharField(max_length=70,null=True)
    valores = models.TextField(max_length=2000,null=True,blank=True)
    filosofiaasociacion= models.TextField(max_length=5000,null=True,blank=True)
    imagen=models.ImageField(upload_to='static/img',blank=True)

    
    def __str__(self):         
        return self.titulomision


class Tallere(models.Model):
    titulo=models.TextField(max_length=5000,null=True,blank=True)
    taller=models.TextField(max_length=5000,null=True,blank=True)
    imagentalleres=models.ImageField(upload_to='static/img',blank=True)

    def __str__(self):         
        return self.titulo








    