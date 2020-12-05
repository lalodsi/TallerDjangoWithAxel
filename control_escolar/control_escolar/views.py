""" Las views es donde esta gran parte de la logica"""
from datetime import datetime
from django.http import HttpResponse
  
def hola(request):
    ahora = datetime.now().strftime('%H')
    return HttpResponse(f'Hola  {ahora}')

def adios (request):
    nombre = 'Diaz Axel'
    year = 2000
    if year == 2020:
        el_regreso = f'{nombre} aun es {year}' 
    else : 
        el_regreso = f'{nombre} felicidades ya no es {year}'
    return HttpResponse(el_regreso)    

def caculos (request):
    x = request.GET['numeros']
    print(type(x))
    return HttpResponse(f'{str(x)}')