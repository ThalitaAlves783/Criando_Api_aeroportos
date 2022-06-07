from django.contrib import admin
from aeroporto.models import Aeroporto

class Aeroportos(admin.ModelAdmin):
    list_display = ('id','nome_aeroporto','codigo_iata','cidade','coodigo_pais_iso','latitude','longitude','altidute')
    list_display_links = ('id','nome_aeroporto')
    search_fields = ('nome_aeroporto','codigo_iata')
    list_per_page = 20

admin.site.register(Aeroporto,Aeroportos)