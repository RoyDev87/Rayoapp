# Generated by Django 4.2.1 on 2023-07-05 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rayoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mecanico',
            name='agnos_exp',
            field=models.IntegerField(null=True, verbose_name='Años Exp.'),
        ),
        migrations.AddField(
            model_name='mecanico',
            name='educacion',
            field=models.TextField(null=True, verbose_name='Educación'),
        ),
        migrations.AddField(
            model_name='mecanico',
            name='nombre',
            field=models.CharField(max_length=100, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='mecanico',
            name='imagen',
            field=models.ImageField(null=True, upload_to='img/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='mecanico',
            name='titulo',
            field=models.CharField(max_length=100, null=True, verbose_name='Titulo'),
        ),
    ]
