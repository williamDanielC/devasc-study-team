import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="dbtaller"
    )

def insertar_linea():
    clave = input("Ingrese el c0digo unico de la linea de investigacion: ")
    nombre = input("Ingrese el nombre de la linea de investigacion: ")
    conexion = conectar_bd()
    cursor = conexion.cursor()
    sql = "INSERT INTO lineainv (clavein, nombre) VALUES (%s, %s)"
    cursor.execute(sql, (clave, nombre))
    conexion.commit()
    print("Linea de investigacion registrada exitosamente.")
    cursor.close()
    conexion.close()

def leer_lineas():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM lineainv")
    print("\n--- Lineas de investigaci0n registradas ---")
    for (clavein, nombre) in cursor:
        print(f"Codigo: {clavein}, Nombre: {nombre}")
    cursor.close()
    conexion.close()

def actualizar_linea():
    clave = input("Ingrese el codigo de la linea de investigacion a actualizar: ")
    nombre = input("Ingrese el nuevo nombre para la linea de investigacion: ")
    conexion = conectar_bd()
    cursor = conexion.cursor()
    sql = "UPDATE lineainv SET nombre = %s WHERE clavein = %s"
    cursor.execute(sql, (nombre, clave))
    conexion.commit()
    print("Linea de investigacion actualizada exitosamente.")
    cursor.close()
    conexion.close()

def eliminar_linea():
    clave = input("Ingrese el codigo de la linea de investigacion a eliminar: ")
    conexion = conectar_bd()
    cursor = conexion.cursor()
    sql = "DELETE FROM lineainv WHERE clavein = %s"
    cursor.execute(sql, (clave,))
    conexion.commit()
    print("Linea de investigacion eliminada exitosamente.")
    cursor.close()
    conexion.close()

def menu():
    while True:
        print("\n--- Menu de Lineas de Investigacion ---")
        print("1. Registrar nueva linea de investigacion")
        print("2. Mostrar todas las lineas de investigaciin")
        print("3. Modificar una linea de investigacion")
        print("4. Eliminar una linea de investigacion")
        print("5. Salir del programa")
        opcion = input("Seleccione una opcion (1-5): ")
        
        if opcion == "1":
            insertar_linea()
        elif opcion == "2":
            leer_lineas()
        elif opcion == "3":
            actualizar_linea()
        elif opcion == "4":
            eliminar_linea()
        elif opcion == "5":
            print("saliendo...")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")

if __name__ == "__main__":
    menu()