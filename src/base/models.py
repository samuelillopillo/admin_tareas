from django.db import models
from django.contrib.auth.models import User


# Definimos las opciones para la prioridad fuera de la clase
PRIORIDAD_CHOICES = (
    ('A', 'Alta'),
    ('M', 'Media'),
    ('B', 'Baja'),
)


class Tarea(models.Model):
    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True,
                                   blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    fecha_vencimiento = models.DateField(null=True, blank=True)
    prioridad = models.CharField(max_length=1, choices=PRIORIDAD_CHOICES, default='M')

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['completo']
