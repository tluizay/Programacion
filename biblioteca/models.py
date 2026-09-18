from django.db import models
class Libro(models.Model):

    titulo = models.CharField("Título", max_length=200)
    autor = models.CharField("autor", max_length=200)
    anio = models.IntegerField("Año")
    disponible = models.BooleanField("Disponible", default=True)

    def __str__(self):
            return self.titulo 
