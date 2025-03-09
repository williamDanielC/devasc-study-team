import mariadb

def conectar():
    try:
        conexion = mariadb.connect(
            host="localhost",
            user="root",
            password="mariadb",
            database="dbtaller",
            port=3305
        )
        return conexion
    except mariadb.Error as e:
        print(f"fallo conexion: {e}")
        return None

def insertar_linea_inv(idlinea, nombreproy):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO lineainv (idlinea, nombreproy) VALUES (?, ?)"
        try:
            cursor.execute(sql, (idlinea, nombreproy))
            conn.commit()
            print("insertada la linea de investigacion correctamente.")
        except mariadb.Error as e:
            print(f"Error al insertar: {e}")
        finally:
            cursor.close()
            conn.close()

def obtener_lineas_inv():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM lineainv"
        try:
            cursor.execute(sql)
            lineas = cursor.fetchall()
            print("\nLista de lineas de Investigacion:")
            for linea in lineas:
                print(f"ID: {linea[0]}, Proyecto: {linea[1]}")
        except mariadb.Error as e:
            print(f"Fallo al obtener datos: {e}")
        finally:
            cursor.close()
            conn.close()

def actualizar_linea_inv(idlinea, nuevo_nombre):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE lineainv SET nombreproy = ? WHERE idlinea = ?"
        try:
            cursor.execute(sql, (nuevo_nombre, idlinea))
            conn.commit()
            print("Actualizada la linea de investigacion.")
        except mariadb.Error as e:
            print(f"Follo al actualizar: {e}")
        finally:
            cursor.close()
            conn.close()

def eliminar_linea_inv(idlinea):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "DELETE FROM lineainv WHERE idlinea = ?"
        try:
            cursor.execute(sql, (idlinea,))
            conn.commit()
            print("Se elimino correctamente la linea de investigacion .")
        except mariadb.Error as e:
            print(f"Fallo al eliminar: {e}")
        finally:
            cursor.close()
            conn.close()

def insertar_tipo_proyecto(tipo):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO tipoproyecto (tipo) VALUES (?)"
        try:
            cursor.execute(sql, (tipo,))
            conn.commit()
            print("Se inserto correctamente el tipo de proyecto .")
        except mariadb.Error as e:
            print(f"Fallo al insertar en tipo de proyecto: {e}")
        finally:
            cursor.close()
            conn.close()

def obtener_tipos_proyecto():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM tipoproyecto"
        try:
            cursor.execute(sql)
            proyectos = cursor.fetchall()
            print("\nLista de Tipos de Proyecto:")
            for proyecto in proyectos:
                print(f"Tipo: {proyecto[0]}")
        except mariadb.Error as e:
            print(f"Fallo al obtener datos: {e}")
        finally:
            cursor.close()
            conn.close()

def eliminar_tipo_proyecto(tipo):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "DELETE FROM tipoproyecto WHERE tipo = ?"
        try:
            cursor.execute(sql, (tipo,))
            conn.commit()
            print("Tipo de proyecto eliminado correctamente.")
        except mariadb.Error as e:
            print(f"Fallo al eliminar de tipoproyecto: {e}")
        finally:
            cursor.close()
            conn.close()

def insertar_profesor(nombreProf):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO profesor (nombreProf) VALUES (?)"
        try:
            cursor.execute(sql, (nombreProf,))
            conn.commit()
            print("Se inserto correctamente Profesor.")
        except mariadb.Error as e:
            print(f"Fallo al insertar profesor: {e}")
        finally:
            cursor.close()
            conn.close()

def obtener_profesores():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM profesor"
        try:
            cursor.execute(sql)
            profesores = cursor.fetchall()
            print("\nLista de Profesores:")
            for profesor in profesores:
                print(f"ID: {profesor[0]}, Nombre: {profesor[1]}")
        except mariadb.Error as e:
            print(f"Erro al obtener datos: {e}")
        finally:
            cursor.close()
            conn.close()

def eliminar_profesor(idprofesor):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "DELETE FROM profesor WHERE idprofesor = ?"
        try:
            cursor.execute(sql, (idprofesor,))
            conn.commit()
            print("Se elimino correctamente Profesor.")
        except mariadb.Error as e:
            print(f"Fallo al eliminar profesor: {e}")
        finally:
            cursor.close()
            conn.close()
if __name__ == "__main__":
    while True:
        print("\n=== CRUD para lineas de Investigacion,Tipos de Proyecto y Profesores ===")
        print("1. Insertar Linea de Investigacion")
        print("2. Mostrar Lineas de Investigacion")
        print("3. Eliminar Linea de Investigacion")
        print("4. Insertar Tipo de Proyecto")
        print("5. Mostrar Tipos de Proyecto")
        print("6. Eliminar Tipo de Proyecto")
        print("7. Insertar Profesor")
        print("8. Mostrar Profesores")
        print("9. Eliminar Profesor")
        print("10. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            idlinea = input("Ingrese el ID de la linea de investigacion: ")
            nombreproy = input("Ingrese el nombre del proyecto: ")
            insertar_linea_inv(idlinea, nombreproy)
        elif opcion == "2":
            obtener_lineas_inv()
        elif opcion == "3":
            idlinea = input("Ingrese el ID de la línea de investigacion a eliminar: ")
            eliminar_linea_inv(idlinea)
        elif opcion == "4":
            tipo = input("Ingrese el tipo de proyecto: ")
            insertar_tipo_proyecto(tipo)
        elif opcion == "5":
            obtener_tipos_proyecto()
        elif opcion == "6":
            tipo = input("Ingrese el tipo de proyecto a eliminar: ")
            eliminar_tipo_proyecto(tipo)
        elif opcion == "7":
            nombreProf = input("Ingrese el nombre del profesor: ")
            insertar_profesor(nombreProf)
        elif opcion == "8":
            obtener_profesores()
        elif opcion == "9":
            idprofesor = input("Ingrese el ID del profesor a eliminar: ")
            eliminar_profesor(idprofesor)
        elif opcion == "10":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
