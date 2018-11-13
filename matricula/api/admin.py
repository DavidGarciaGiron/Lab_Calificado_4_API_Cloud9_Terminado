from django.contrib import admin

# Register your models here.
from .models import Persona

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'correo', 'tipo', 'detalle')

admin.site.register(Persona, PersonaAdmin)
