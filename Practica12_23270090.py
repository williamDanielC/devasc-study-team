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
            print(f"Fallo al insertar: {e}")
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

def actualizar_tipo_proyecto(tipo_actual, nuevo_tipo):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE tipoproyecto SET tipo = ? WHERE tipo = ?"
        try:
            cursor.execute(sql, (nuevo_tipo, tipo_actual))
            conn.commit()
            print("Se actualizado correctamente el Tipo de proyecto .")
        except mariadb.Error as e:
            print(f"Fallo al actualizar: {e}")
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
            print(f"Fallo al obtener datos: {e}")
        finally:
            cursor.close()
            conn.close()

def actualizar_profesor(idprofesor, nuevo_nombre):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE profesor SET nombreProf = ? WHERE idprofesor = ?"
        try:
            cursor.execute(sql, (nuevo_nombre, idprofesor))
            conn.commit()
            print("Se actualizado correctamente el Profesor .")
        except mariadb.Error as e:
            print(f"Error al actualizar: {e}")
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

def insertar_profesor_proy(idprofesor, clave, calificacion, rol):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO profesorproy (idprofesor, clave, calificacion, rol) VALUES (?, ?, ?, ?)"
        try:
            cursor.execute(sql, (idprofesor, clave, calificacion, rol))
            conn.commit()
            print("Se insertada correctamente  la relacion Profesor-Proyecto.")
        except mariadb.Error as e:
            print(f"Fallo al insertar: {e}")
        finally:
            cursor.close()
            conn.close()

def obtener_profesores_proy():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM profesorproy"
        try:
            cursor.execute(sql)
            relaciones = cursor.fetchall()
            print("\nLista de Relaciones Profesor-Proyecto:")
            for relacion in relaciones:
                print(f"ID Profesor: {relacion[0]}, Clave Proyecto: {relacion[1]}, Calificación: {relacion[2]}, Rol: {relacion[3]}")
        except mariadb.Error as e:
            print(f"Fallo al obtener datos: {e}")
        finally:
            cursor.close()
            conn.close()

def actualizar_profesor_proy(idprofesor, clave, calificacion, rol):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE profesorproy SET calificacion = ?, rol = ? WHERE idprofesor = ? AND clave = ?"
        try:
            cursor.execute(sql, (calificacion, rol, idprofesor, clave))
            conn.commit()
            print("Se actualiso correctamente la relacion Profesor-Proyecto.")
        except mariadb.Error as e:
            print(f"Fallo al actualizar: {e}")
        finally:
            cursor.close()
            conn.close()

def eliminar_profesor_proy(idprofesor, clave):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        sql = "DELETE FROM profesorproy WHERE idprofesor = ? AND clave = ?"
        try:
            cursor.execute(sql, (idprofesor, clave))
            conn.commit()
            print("Se elimino correctamente la relacion Profesor-Proyecto .")
        except mariadb.Error as e:
            print(f"Fallo al eliminar: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    while True:
        print("\n=== CRUD de lineas Investigacion, Tipos de Proyecto, Profesores y Profesor-Proyecto ===")
        print("\n1. Agregar nueva linea de investigacion")
        print("2. Mostrar las loneas de investigacion")
        print("3. Actualizar linea de Investigacion")
        print("4. Eliminar linea de Investigacion")
        print("\n5. Agregar nuevo tipo de proyect")
        print("6. Mostrar los tipos de Proyecto")
        print("7. Actualizar Tipo de Proyecto")
        print("8. Eliminar Tipo de Proyecto")
        print("\n9. Agregar nuevo profesor")
        print("10. Mostrar Profesores")
        print("11. Actualizar Profesor")
        print("12. Eliminar Profesor")
        print("\n13. Asignar Profesor-Proyecto")
        print("14. Mostrar Relaciones Profesor-Proyecto")
        print("15. Actualizar relacion Profesor-Proyecto")
        print("16. Eliminar relacion Profesor-Proyecto")
        print("17. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            idlinea = input("Ingrese el ID de la nueva linea de investigacion: ")
            nombreproy = input("Ingrese el nombre del proyecto: ")
            insertar_linea_inv(idlinea, nombreproy)
        elif opcion == "2":
            obtener_lineas_inv()
        elif opcion == "3":
            idlinea = input("Ingrese el ID de la linea de investigacion a actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del proyecto: ")
            actualizar_linea_inv(idlinea, nuevo_nombre)
        elif opcion == "4":
            idlinea = input("Ingrese el ID de la linea de investigacion a eliminar: ")
            eliminar_linea_inv(idlinea)
        elif opcion == "5":
            tipo = input("Ingrese el tipo de proyecto: ")
            insertar_tipo_proyecto(tipo)
        elif opcion == "6":
            obtener_tipos_proyecto()
        elif opcion == "7":
            tipo_actual = input("Ingrese el tipo de proyecto a actualizar: ")
            nuevo_tipo = input("Ingrese el nuevo tipo de proyecto: ")
            actualizar_tipo_proyecto(tipo_actual, nuevo_tipo)
        elif opcion == "8":
            tipo = input("Ingrese el tipo de proyecto a eliminar: ")
            eliminar_tipo_proyecto(tipo)
        elif opcion == "9":
            nombreProf = input("Ingrese el nombre del profesor: ")
            insertar_profesor(nombreProf)
        elif opcion == "10":
            obtener_profesores()
        elif opcion == "11":
            idprofesor = input("Ingrese el ID del profesor a actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del profesor: ")
            actualizar_profesor(idprofesor, nuevo_nombre)
        elif opcion == "12":
            idprofesor = input("Ingrese el ID del profesor a eliminar: ")
            eliminar_profesor(idprofesor)
        elif opcion == "13":
            idprofesor = input("Ingrese el ID del profesor: ")
            clave = input("Ingrese la clave del proyecto: ")
            calificacion = float(input("Ingrese la calificación: "))
            rol = input("Ingrese el rol del profesor en el proyecto: ")
            insertar_profesor_proy(idprofesor, clave, calificacion, rol)
        elif opcion == "14":
            obtener_profesores_proy()
        elif opcion == "15":
            idprofesor = input("Ingrese el ID del profesor: ")
            clave = input("Ingrese la clave del proyecto: ")
            calificacion = float(input("Ingrese la nueva calificación: "))
            rol = input("Ingrese el nuevo rol del profesor en el proyecto: ")
            actualizar_profesor_proy(idprofesor, clave, calificacion, rol)
        elif opcion == "16":
            idprofesor = input("Ingrese el ID del profesor: ")
            clave = input("Ingrese la clave del proyecto: ")
            eliminar_profesor_proy(idprofesor, clave)
        elif opcion == "17":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
