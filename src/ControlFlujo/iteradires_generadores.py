# Ejemplo 1 de los iteradores

numeros =  [1, 2, 3, 4, 5]
iterador = iter(numeros)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))


# Ejemplo 2 iteradores en cadenas 

texto = "Hola Mundo"

iter_texto = iter(texto)

for char in texto:
    print(char)

# Ejemplo 3 crear un iterador para número impares

limite = 10

#crear el iterador
odd_iter = iter(range(1, limite, 2)) 

for i in odd_iter:
    print(i)


# Generadores 

def generador():
    yield 1
    yield 2
    yield 3

for valor in generador():
    print(valor)

# Generador de la serie de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacci(limite):
    x, y = 0, 1
    while x < limite:
        yield x
        x, y = y, x + y

for numero  in fibonacci(100):
    print(numero)
   
