from django.db import models

class usuario(models.Model):
    Id_Usuario = models.AutoField(
        primary_key = True,
        db_column='Id_Usuario' 
    )
    Correo_Usuario = models.CharField(
        max_length=100,
        db_column='Correo_Usuario'
    )
    Contrasena_Usuario = models.CharField(
        max_length=255,
        db_column='Contrasena_Usuario'
    )
    Rol_Usuario = models.CharField(
        max_length=20,
        db_column='Rol_Usuario'
    )
    Estado_Usuario = models.BooleanField(
        db_column='Estado_Usuario'
    )
    Fecha_Registro = models.DateTimeField(
        db_column='Fecha_Registro',
        null= True,
        blank=True
    )
    class Meta:
        managed = False
        db_table = 'USUARIO'

    def __str__(self):
        return self.Correo_Usuario

class Cliente (models.Model):
    Id_Cliente = models.AutoField(
        primary_key= True,
        db_column= 'Id_Cliente'
    )        
    usuario = models.ForeignKey(
        usuario,
        on_delete=models.DO_NOTHING,
        db_column='Id_Usuario',
        related_name='clientes',
        db_constraint= False
    )
    Nombre_Cliente = models.CharField(
        max_length= 100,
        db_column='Nombre_Cliente'
    )
    Telefono_Cliente = models.CharField(
            max_length= 20,
            db_column='Telefono_Cliente',
            null=True,
            blank=True
    ) 
    Fecha_Nacimiento = models.DateField(
            max_length= 100,
            db_column='Fecha_Nacimiento',
            null= True,
            blank= True
    ) 
    Estado_Cliente = models.BooleanField(
            db_column='Estado_Cliente'              
    )
    Fecha_Registro = models.DateTimeField(
            db_column='Fecha_registro',
            null= True,
            blank= True
    )

    class Meta:
        managed = False
        db_table = 'CLIENTE'

    def __str__(self):
        return self.Nombre_Cliente




# Create your models here.
