""""Views de la la aplicacion matricula"""

#importando render
from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
#utlidades 
from datetime import datetime

#Datos Pruba
grupos =[
    {
        'Grupo' :' A ',
        'Profesora': ' Martha',
        'Salon' :'303',
        'Limpieza': 'Miguel'

    },
    {
        'Grupo' :' B ',
        'Profesora': ' Lizbeth',
        'Salon' :'509',
        'Limpieza': 'Miguel'

    },
    {
        'Grupo' :' C ',
        'Profesora': ' Esther',
        'Salon' :'555',
        'Limpieza': 'Sara'

    }
]

  #"""Lista los grupos que existe en la escuela"""
   # contenido = [ ]
    #for grupo in grupos:
     #   contenido.append("""
      #      <p><strong> {Grupo}</strong></p>
       #     <p><small> {Profesora}</small></p>
        #    <p><small> {Salon}</small></p>
         #   <p><small> {Limpieza}</small></p>
          #  """.format(**grupo))

#Manda los grupos registrados
def lista_de_grupos(request):
  
    
    return render(request,'inicio.html',{'grupos':grupos})