# Programación en lenguajes estructurados en aplicaciones de gestión
## Parte 1
La parte 1 esta destallada en el archivo biblioteca/CRUD-parte1.py, es un pequeño pragrama donde aplicamos la logica de python para insertar datos y mostrar datos en json
## Parte 2
La interfaz web de la biblioteca, tengo varias plantillas en template/
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

## Parte 4 
En esta sección he creado el modelo Libro.
 Comandos para las migraciones :
 python manage.py makemigrations
 python manage.py migrate

recopilar archivos estaticos:
