def calcular_total(carrito):
    total = sum(carrito.values())
    return total
carrito = {}
while True:
    articulo = input("Ingrese el nombre del artículo (o 'pagar' para finalizar la compra): ")
    if articulo.lower() == 'pagar':
        break
    precio = float(input("Ingrese el precio del artículo: "))
    carrito[articulo] = precio
print("\nLista de la compra:")
for articulo, precio in carrito.items():
    print(f"{articulo}: ${precio}")
total_pagar = calcular_total(carrito)
print(f"\nTotal a pagar: ${total_pagar}")
