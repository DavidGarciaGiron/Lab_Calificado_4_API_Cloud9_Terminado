from django.db import models

# Create your models here.
class Persona (models.Model):
    
    id=models.AutoField(primary_key=True)
    correo=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)
    detalle=models.TextField(null=True)
    
    class Meta:
        db_table ="personas"
        
    def __str__(self):
        return self.nombre
    
