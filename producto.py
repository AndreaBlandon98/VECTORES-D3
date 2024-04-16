precios_productos = {
    "manzanas": 2.5,
    "plátanos": 1.99,
    "naranjas": 3.0,
    "peras": 2.0,
    "uvas": 4.5
}
producto = input("Ingrese el nombre del producto: ").lower()
cantidad = int(input("Ingrese el número de productos: "))
if producto in precios_productos:
    precio_total = precios_productos[producto] * cantidad
    print(f"El precio total de {cantidad} {producto} es: ${precio_total}")
else:
    print("El producto ingresado no está en el diccionario de precios.")