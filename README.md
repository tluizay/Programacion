# Programación en lenguajes estructurados en aplicaciones de gestión
## Parte 1: Gestión básica de libros
La parte 1 esta destallada en el archivo biblioteca/CRUD-parte1.py, es un pequeño pragrama donde aplicamos la logica de python para insertar datos y mostrar datos en json. Me parecio mas comodo de esta manera para no perder los datos en el proceso.

## Parte 2: Interfaz web de biblioteca
La interfaz web de la biblioteca, tengo varias plantillas en template/, a su vez core/ quien contiene el inicio, componentes quien contiene footer y navbar, y libros quien contiene, editar, eliminar,detalle de libro y nuevo libro. 
## Parte 3: 
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
python manage.py collectstatic

configure el despliegue en un archivo entorno.py en la carpeta config, se encarga de inyectar los datos en setting de forma segura desde el .env