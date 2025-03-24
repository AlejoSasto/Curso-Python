#
#
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# posición 0. 1, 2, ..., 9
# i el velor 1, 2, 3, ..., 10


numeros =  [1, 2, 3, 4, 5]

for i in numeros:
    print("El valor de i es: ", i)

for i in range(4,10):
    print("El valor de i es: ", i)


frutas = ["Mango", "Manzana", "Fresa", "Naranja"]

for fruta in frutas:
    print("La fruta es:", fruta)
    if fruta == "Manzana":
        print("Se encontró la manzana")
        break

# Ciclo While

contador = 0

while contador < 10:
    if contador == 8:
        break
    print("El valor de contador es:", contador)
    contador +=1

for i in numeros:
    if i == 3:
        pass
    print("El valor de i es: ", i)