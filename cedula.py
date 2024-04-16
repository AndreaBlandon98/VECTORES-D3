documentos_votantes = [111111111, 222222222, 333333333, 444444444, 555555555]
def buscar_documento(documento):
    for doc in documentos_votantes:
        if doc == documento:
            return True
            return False

documento_ingresado = int(input("Ingrese su número de documento de identidad: "))
if buscar_documento(documento_ingresado):
    print("Usted puede votar en las elecciones presidenciales de este año.")
else:
    print("Usted no puede votar en las elecciones presidenciales de este año.")

