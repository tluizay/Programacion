import json 

libros= []

def guardar_libros():
    with open("libros.json", "w", encoding="utf-8") as archivo:
        #el libro se guarda/crea donde está el archivo,
        #menos si estás editando en VSC que se guarda/crea 
        #donde tienes la carpeta abierta como carpeta principal
        json.dump(libros, archivo, indent=4,ensure_ascii=False)

def cargar_libros():
    global libros
    try:
        with open("libros.json", "r", encoding = "utf-8") as archivo:
            libros = json.load(archivo)
    except FileNotFoundError:
        libros = []
        
def nuevo_libro(disponible,titulo,autor,anio):
    escribir =  True
    nuevo_libro = {'disponible':disponible, 'titulo': titulo, 'autor':autor, 'anio':anio}
    for libro in libros:
        if libro["id_libro"] == nuevo_libro["id_libro"]:
            print("Ese ISBN ya existe, " \
            "o ya tienes el libro o te has equivocado de ISBN")
            escribir = False
            return
    if escribir:
        libros.append(nuevo_libro)
        guardar_libros()
        print("Libro añadido con éxito.")
        return

def mostrar_libros():
    if not libros:
        print("No hay libros registrados.")
        return
    for libro in libros:
        print(("*")*40)
        print(f"Disponible: {libro['disponible']}")
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Año: {libro['anio']}")
        print('*'*40)
    return

def libros_disponibles():
    for libro in libros:
        if libro["disponible"] == True:
            print("*" * 40)
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Año: {libro['anio']}")
            print("*" * 40)
            return

    print("NO hay libros disponibles ahora")  

def buscar_libro(titulo):
    
    for libro in libros:
        if libro["titulo"] == titulo:
            print("*" * 40)
            print(f"Disponible: {libro['disponible']}")
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Año: {libro['anio']}")
            print("*" * 40)
            return

    print("El libro no está en la biblioteca.")
      
while True:
    print('='*40)
    print('Menú de opciones biblioteca')
    print('1.Crear libro')
    print('2.Mostrar libros')
    print('3·Buscar libro')
    print('4.Libros disponibles')
    print('5.Salir')
    print('*'*40)
    opcion=input('Que opción eliges: ')


    match opcion:
        case "1":
            print('si el libro NO esta disponible presiona enter')
            print('si el libro SI esta disponible escribe si, s,true o 1')
            disponible = input('Disponible: ').lower() in ('si', 's', 'true', '1')   
            titulo = input('Título: ').capitalize()
            autor = input('Autor: ').capitalize()
            anio = input('Año: ')
            nuevo_libro(disponible,titulo,autor,anio)
            
        case "2":
            mostrar_libros()
        case "3":
            titulo= input("Qué libro buscas: ").capitalize()
            buscar_libro(titulo)
        case "4":
            libros_disponibles()
        case "5":
            break
        case _:
            print("Opción no reconocida.")

#si estas aqui, bendiciones 