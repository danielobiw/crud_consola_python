import mysql.connector
from mysql.connector import Error


class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="XXXX", # AQUI SE INGRESA EL HOST AL QUE SE CONECTA EL GESTOR DE BD
                port="0000",  # AQUI SE INGRESA EL PUERTO AL QUE SE CONECTA EL GESTOR DE BD
                user="XXXX",  # AQUI SE INGRESA EL USUARIO DEL GESTOR DE BD
                password="XXXX",  # AQUI SE INGRESA LA CLAVE O PASSWORD DEL GESTOR DE BD
                database="XXXX" # AQUI SE INGRESA EL NOMBRE DE LA BD
            )
        except Error as ex:
            print("Error de conexion: {0}".format(ex))

    def listarJuegos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM juegos ORDER BY id ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error de conexion: {0}".format(ex))

    def registrarJuego(self, juego):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(
                    "INSERT INTO juegos "
                    "(nombre, voces, textos, consola, formato, comentarios) "
                    "VALUES (%s, %s, %s, %s, %s, %s)",
                    juego
                )
                self.conexion.commit()
                cursor.close()
                print("¡Juego registrado con exito!\n")
            except Error as ex:
                print(f"Error al registrar juego: {ex}")

    def actualizarJuego(self, juego):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE juegos SET nombre=%s, voces=%s, textos=%s, consola=%s, formato=%s, comentarios=%s WHERE id=%s"
                cursor.execute(sql, (juego[0], juego[1], juego[2], juego[3], juego[4], juego[5], juego[6]))
                self.conexion.commit()
                cursor.close()
                print("¡Juego actualizado con exito!\n")
            except Error as ex:
                print(f"Error al registrar juego: {ex}")

    def eliminarJuego(self, idJuego):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM juegos WHERE id = %s"
                cursor.execute(sql, (idJuego,))
                self.conexion.commit()
                cursor.close()
                print("¡Juego eliminado con exito!\n")
            except Error as ex:
                print(f"Error al eliminar juego: {ex}")

