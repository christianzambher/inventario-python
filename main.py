from database import crear_tabla

from helpers import (
    agregar_producto,
    mostrar_productos,
    buscar_producto,
    actualizar_stock,
    eliminar_producto
)

def menu():
    while True:
        print("""
===== INVENTARIO =====

1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Actualizar stock
5. Eliminar producto
6. Salir
""")

        opcion = input("Opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_stock()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("Sistema cerrado")
            break
        else:
            print("Opción inválida")

crear_tabla()
menu()