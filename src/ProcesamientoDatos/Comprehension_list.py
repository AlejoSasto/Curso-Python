# list Comprehensions

# Estructura básica 
# [expresion for item in iterable if condicion] [x f i]


numeros = [1, 2, 3, 4, 5, 6]
# cuadrado = [x**2 for x in numeros]
cuadrado = [x**2 for x in range(1,7)]
print(cuadrado)


pares = [x for x in numeros if x % 2 == 0 ]
print(pares)

# Caso 1 conversión de celsius a fahrenheit
# f = c * 9/5 + 32

celsius = [0, 10, 20, 30, 40, 50]
fahrenheit = [(temp * 9/5 )+ 32 for temp in celsius]
print(fahrenheit)

# Caso 2 Hallar la transpuesta de una matriz

matriz = [[1, 2, 3],
          [4, 5, 6], 
          [7, 8, 9]]

# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]

transpuesta = [[row[i] for row in matriz] for i in range(len(matriz[0]))]
# print(transpuesta)

# Normalmente 

transpuesta = []
for i in range(len(matriz[0])):
    transpuesta_row = []
    for row in matriz:
        transpuesta_row.append(row[i])
    transpuesta.append(transpuesta_row)

print(transpuesta)