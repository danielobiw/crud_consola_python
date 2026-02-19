from BD.conexion import DAO
import funciones


def menu():
    continuar=True
    while (continuar):
        print("======== MENÚ PRINCIPAL ========")
        print("1. Listar juegos")
        print("2. Registrar juego")
        print("3. Actualizar juego")
        print("4. Eliminar juego")
        print("5. Salir del menú")
        print("================================")

        try:
            opcion=int(input("Seleccione una opcion: "))
        except ValueError:
            print("Debe ingresar un valor del menú")
            continue

        if opcion<1 or opcion>5:
            print("Opcion incorrecta. Intente nuevamente")
        elif opcion==5:
            print("¡Chao!")
            continuar=False
        else:
            ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    dao=DAO()

    match opcion:
        case 1:
            try:
                juegos = dao.listarJuegos()
                if len(juegos) > 0:
                    funciones.listarJuegos(juegos)
                else:
                    print("No se encontraron juegos")
            except:
                print("¡Ha ocurrido un error!")

        case 2:
            juego = funciones.pedirDatosRegistro()
            try:
                dao.registrarJuego(juego)
            except Exception as ex:
                print("¡Ha ocurrido un error!", ex)

        case 3:
            try:
                juegos = dao.listarJuegos()
                if len(juegos) > 0:
                    juego = funciones.pedirDatosActualizar(juegos)
                    if juego:
                        dao.actualizarJuego(juego)
                    else:
                        print("Juego no encontrado")
                else:
                    print("No se encontraron juegos")
            except:
                print("¡Ha ocurrido un error!")

        case 4:
            try:
                juegos = dao.listarJuegos()
                if len(juegos) > 0:
                    juego = funciones.pedirDatosEliminar(juegos)
                    if juego:
                        dao.eliminarJuego(juego)
                    else:
                        print("Juego no encontrado")
                else:
                    print("No se encontraron juegos")
            except:
                print("¡Ha ocurrido un error!")


menu()

