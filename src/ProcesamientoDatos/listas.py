lista=[]

lista = ["Viajandro a la universodad",
         "Tomando onces en la plazoleta de la universidad",
         "Ir a clase en la Universidad",
         "Volver a casas"]

print(lista)
numeros = [ 5, 10, 50, 6, 3, 1, "Cinco", True]
print(type(numeros))
print(numeros)
lista_mixta = [5, 10.3, 50.55, 6, 3, 1, "Cinco", True]
print("Pimer elemento de la lista:", lista_mixta[0])
print("Segundo elemento de la lista:", lista_mixta[1])
print("Ultimo elemento de la lista", lista_mixta[-1])
cadenas = "Hola mundo"
print("Pimer elemento de la cadenas:", cadenas[0])
print("Segundo elemento de la cadenas:", cadenas[1])
print("Ultimo elemento de la cadenas", cadenas[-1])
print(lista_mixta[0:2])
print(lista_mixta[:5])
print(lista_mixta[0:])
lista_mixta.append(False)
print(lista_mixta)
lista_mixta.append(["Hola", "Mundo"])
print(lista_mixta)
lista_mixta.insert(2, "Nuevo elemento")
print(lista_mixta)
lista_mixta.index(["Hola", "Mundo"])
print(lista_mixta)

lista_numeros = [5, 10, 55, 6, 3, 1]
print(len(lista_numeros))
print(lista_numeros)
print("Número mayor", max(lista_numeros))
print("Número menor", min(lista_numeros))
del lista_numeros[2]
print(lista_numeros)    
del lista_numeros[2:4]
print(lista_numeros)
del lista_numeros
print(lista_numeros)