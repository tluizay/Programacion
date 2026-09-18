# Programación en lenguajes estructurados en aplicaciones de gestión
## Parte 1
## Parte 2
## Parte 3 
Consulta ORM:

```text
Mostrar todos los libros
>>> from biblioteca.models import Libro   
>>> libro = Libro.objects.all()
>>> print(libro)
<QuerySet []>


Agregar un libro
>>> Libro.objects.create(
...     titulo="hola",
...     autor="luizay",
...     anio="2026",
...     disponible=True)
<Libro: hola>

Mostrar libros disponibles
>>> from biblioteca.models import Libro
>>> libro=Libro.objects.filter(disponible=True)
>>> print(libro)
<QuerySet [<Libro: hola>]>

```

# Parte 4 
