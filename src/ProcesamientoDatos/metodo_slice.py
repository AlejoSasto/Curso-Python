lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_b = lista_a

print(lista_a)
print(lista_b)

del lista_a[0]

print(id(lista_a))
print(id(lista_b))

lista_C = lista_a[:]

print(id(lista_a))
print(id(lista_b))
print(id(lista_C))

lista_a.append(11)

print(lista_a)
print(lista_b)
print(lista_C)