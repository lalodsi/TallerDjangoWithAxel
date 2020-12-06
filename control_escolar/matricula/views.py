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
co={

}

def lista_de_grupos(request):
  
    
    return render(request,'inicio.html',{'grupos':grupos})

def index(request):
    return render(request,'index.html',co)