

def listarJuegos(juegos):
    print("\n======== LISTA DE JUEGOS ========")
    for juego in juegos:
        datos = "Id: {0}. Nombre: {1} - Voces: {2} - Textos: {3} - Consola: {4} - Formato: {5} - Comentarios: {6}"
        # LA SIGUIENTE LINEA ES OTRA FORMA DE PRESENTAR LOS DATOS
        # datos="Id: {0} \nNombre: {1} \nVoces: {2} \nTextos: {3} \nConsola: {4} \nFormato: {5} \nComentarios: {6}\n"
        print(datos.format(juego[0], juego[1], juego[2], juego[3], juego[4], juego[5], juego[6]))
    print("\n")

def pedirDatosRegistro():
    nombre = input("Ingrese el nombre del juego: ")
    voces = input("Ingrese el idioma de audio del juego: ")
    textos = input("Ingrese el idioma de textos del juego: ")
    consola = input("Ingrese la consola del juego: ")
    formato = input("Ingrese el formato del juego: ")
    comentarios = input("Ingrese comentarios para el juego: ")

    juego = (nombre, voces, textos, consola, formato, comentarios)
    return juego

def pedirDatosActualizar(juegos):
    listarJuegos(juegos)
    existeId = False
    idActual = int(input("Ingrese el id del juego a actualizar:"))
    for juego in juegos:
        if juego[0]==idActual:
            existeId = True
            break
    if existeId:
        print("\nIngrese los nuevos datos del juego:")
        nombre = input("nombre: ")
        voces = input("idioma de voces: ")
        textos = input("idioma de textos: ")
        consola = input("consola: ")
        formato = input("formato: ")
        comentarios = input("comentarios: ")

        juego=(nombre, voces, textos, consola, formato, comentarios, idActual)

    else:
        juego=None

    return juego

def pedirDatosEliminar(juegos):
    listarJuegos(juegos)
    existeId = False
    idActual = int(input("Ingrese el id del juego a eliminar: "))
    for juego in juegos:
        if juego[0] == idActual:
            existeId = True
            break
    if existeId:
        idEliminar = idActual
    else:
        idEliminar = None

    return idEliminar

