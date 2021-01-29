from django.shortcuts import render
from django.http import HttpResponse
from appproyecto.models import Motocicleta

# Create your views here.

def ingresar_moto(request):
    return render(request,'ingresar_moto.html')

def eliminar_moto(request):
    return render(request,'eliminar_moto.html')

def modificar_moto(request):
    return render(request,'modificar_moto.html')

def listar_moto(request):
    return render(request, 'listar_moto.html')

def categorias(resquest):
    return render(request, 'Categorias.html')

def cotizar(resquest):
    return render(request, 'cotizar.html')
    
def GaleriaDeImagenes(resquest):
    return render(request, 'GaleriaDeImagenes.html')

def index(resquest):
    return render(request, 'index.html')

def QuienesSomos(resquest):
    return render(request, 'QuienesSomos.html')

def ingreso_moto(request):
    nombre=request.GET['txt_nombre_moto']
    modelo=request.GET['txt_modelo_moto']
    velocidad=request.GET['txt_velocidad_moto']
    cambio=request.GET['txt_cambio_moto']
    precio=request.GET['txt_precio']
    if len(nombre)>0 and len(modelo)>0 and len(velocidad)>0 and len(cambio)>0 and len(precio)>0 :
        pro=Motocicleta(nombre=nombre,modelo=modelo,velocidad=velocidad,cambio=cambio,precio=precio)
        pro.save()
        mensaje='motocicleta ingresada correctamente'
    else:
        mensaje='motocicleta no ingresada. faltan campos por cubrir'
    return HttpResponse(mensaje)


def eliminacion_motocicleta(request):
    if request.GET['txt_id']:
        id_recibido=request.GET['txt_id']
        producto=Motocicleta.objects.get(id=id_recibido)
        if producto:
            pro=Motocicleta.objects.get(id=id_recibido)
            pro.delete()
            mensaje='Motocicleta eliminada corecctamente'
        else:
            mensaje='Motocicleta no eliminada no se enuentra el id'
    else:
        mensaje='Debe ingresar un id'
    return HttpResponse(mensaje)

def modificar(request):
    if request.GET['txt_id']:
        id_recibido=request.GET['txt_id']
        precio_recibido=request.GET['txt_precio']
        producto=Motocicleta.objects.filter(id=id_recibido)
        if producto:
            pro=Motocicleta.objects.get(id=id_recibido)
            pro.precio=precio_recibido
            pro.save()
            mensaje='precio motocicleta correctamente modificado'
            return HttpResponse(mensaje)
        else:
            mensaje='no existe producto para modificar'
            return HttpResponse(mensaje)
    else:
        mesanje='debe ingresar un id valido'
        return HttpResponse(mensaje)

def lista_motocicleta(request):
    articulos=Motocicleta.objects.all()
    return render(request,'listar_moto.html',{'articulos':articulos})
