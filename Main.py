from pymongo import MongoClient # El cliente de MongoDB
from Producto import Producto # La clase Producto
from bson.objectid import ObjectId # Para crear ObjectId, porque _id como cadena no funciona

def obtener_bd():
        # PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
        mongoClient = MongoClient('localhost',27017)

        # PASO 2: Conexión a la base de datos
        db = mongoClient.mitienda

        # PASO 3: Obtenemos una coleccion para trabajar con ella
        collection = db.productos
        
        return db



def insertar(producto):
    base_de_datos = obtener_bd()
    productos = base_de_datos.productos
    return productos.insert_one({
        "nombre": producto.nombre,
        "valor": producto.valor,
        "stock": producto.stock,
        }).inserted_id

def obtener():
    base_de_datos = obtener_bd()
    return base_de_datos.productos.find()

def actualizar(id, producto):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.productos.update_one(
        {
        '_id': ObjectId(id)
        }, 
        {
            '$set': {
                "nombre": producto.nombre,
                "valor": producto.valor,
                "stock": producto.stock,
            }
        })
    return resultado.modified_count

def eliminar(id):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.productos.delete_one(
        {
        '_id': ObjectId(id)
        })
    return resultado.deleted_count


menu = """Bienvenido a la tienda.
1 - Insertar producto
2 - Ver todos
3 - Actualizar
4 - Eliminar
5 - Salir
"""
eleccion = None

while eleccion is not 5:
    print(menu)
    eleccion = int(input("Elige: "))
    if eleccion is 1:
        print("Insertar")
        nombre = input("Nombre del producto: ")
        valor = float(input("Valor del producto: "))
        stock = float(input("Stock del producto: "))
        producto = Producto(nombre, valor, stock)
        id = insertar(producto)
        print("El id del producto insertado es: ", id)
    elif eleccion is 2:
        print("Obteniendo productos...")
        for producto in obtener():
            print("=================")
            print("Id: ", producto["_id"])
            print("Nombre: ", producto["nombre"])
            print("Valor: ", producto["valor"])
            print("Stock: ", producto["stock"])
    elif eleccion is 3:
        print("Actualizar")
        id = input("Dime el id: ")
        nombre = input("Nuevo nombre del producto: ")
        valor = float(input("Nuevo valor del producto: "))
        stock = float(input("Nueva stock del producto: "))
        producto = Producto(nombre, valor, stock)
        productos_actualizados = actualizar(id, producto)
        print("Número de productos actualizados: ", productos_actualizados)

    elif eleccion is 4:
        print("Eliminar")
        id = input("Dime el id: ")
        productos_eliminados = eliminar(id)
        print("Número de productos eliminados: ", productos_eliminados)