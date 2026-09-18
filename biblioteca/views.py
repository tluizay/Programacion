from django.shortcuts import render, get_object_or_404,redirect
from .models import Libro
from .forms import LibroForm
from django.contrib import messages
 
def inicio(request):
    return render(request, 'core/inicio.html')

def listar_libros(request):

    libros = Libro.objects.all()
    libros_disponibles = Libro.objects.filter(disponible=True)   
    contexto = {
        "libros": libros,
        "libros_disponibles":libros_disponibles,
    }

    return render(
        request,
        "libros/libros_lista.html",
        contexto
    )

def nuevo_libro(request):
    if request.method == "POST":

        formulario = LibroForm(request.POST)

        if formulario.is_valid():

            formulario.save()
            messages.success(self.request, "Libro creador")
            return redirect("libros_lista")

    else:

        formulario = LibroForm()

    return render(
        request,
        "libros/nuevo_libro.html",
        {
            "formulario": formulario
        }
    )

def eliminar_libro(request, pk):

    libro = get_object_or_404(
        Libro,
        titulo=libro,
        pk=pk
    )

    if request.method == "POST":

        libro.delete()
        messages.error(self.request, "Libro eliminadp")
        return redirect("libros_lista")

    return render(
        request,
        "libros/eliminar_libro.html",
        {
            "libro": libro
        }
    )
