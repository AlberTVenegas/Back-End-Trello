from django.db import models

# Create your models here.





class Tablero(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Comentario(models.Model):
    tarea = models.ForeignKey('Tarea', on_delete=models.CASCADE, related_name='comentarios')
    content = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
 

class Tarea(models.Model):
    tablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)   


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    
