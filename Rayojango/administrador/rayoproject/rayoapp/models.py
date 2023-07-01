from django.db import models

# Create your models here.


class Mecanico(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    descripcion = models.TextField(verbose_name="Descipción", null=True)
    imagen = models.ImageField(
        upload_to='img/', verbose_name="Imagen", null=True)

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descipción: " + self.descripcion
        return fila

    # INSTRUCCION PARA BORRAR LA IMAGEN DEL MECANICO, LA ELIMINA DEL SOTRAGE
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
