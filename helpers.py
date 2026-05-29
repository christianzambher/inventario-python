from database import conectar

# Agregar un nuevo producto a la base de datos
def agregar_producto():
    try:
        nombre = input("Nombre producto: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", (nombre, precio, stock))
        conexion.commit()
        conexion.close()

        print("Producto agregado exitosamente")
    except ValueError:
        print("Datos invalidos")

# Mostrar todos los productos disponibles en la base de datos
def mostrar_productos():
    conexion = conectar()

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")

    productos = cursor.fetchall()

    conexion.close()

    if not productos:
        print("No hay productos")
        return

    for producto in productos:
        print(
            f"""
ID: {producto[0]}
Nombre: {producto[1]}
Precio: ${producto[2]}
Stock: {producto[3]}
------------------------
""")

# Buscar productos por nombre utilizando una consulta SQL con LIKE
def buscar_producto():
    nombre = input("Producto buscar: ")

    conexion = conectar()

    cursor = conexion.cursor()
    cursor.execute("""
    SELECT * FROM productos
    WHERE nombre LIKE ?
    """, (f"%{nombre}%",))

    productos = cursor.fetchall()

    conexion.close()

    if productos:
        for producto in productos:
            print(producto)
    else:
        print("Producto no encontrado")

# Actualizar el stock de un producto específico utilizando su ID
def actualizar_stock():
    try:
        id_producto = int(input("ID producto: "))
        nuevo_stock = int(input("Nuevo stock: "))

        conexion = conectar()

        cursor = conexion.cursor()
        cursor.execute("""
        UPDATE productos
        SET stock = ?
        WHERE id = ?
        """, (nuevo_stock, id_producto))

        conexion.commit()
        conexion.close()

        print("Stock actualizado")
    except ValueError:
        print("Datos inválidos")

# Eliminar un producto de la base de datos utilizando su ID
def eliminar_producto():
    try:
        id_producto = int(input("ID eliminar: "))

        conexion = conectar()

        cursor = conexion.cursor()
        cursor.execute("""
        DELETE FROM productos
        WHERE id = ?
        """, (id_producto,))

        conexion.commit()

        conexion.close()

        print("Producto eliminado")
    except ValueError:
        print("ID inválido")