x = 10

# if x > 10:
#     print("X ES MAYOR QUE 10")
# elif x == 10:
#     print("X ES IGUAL A 10")  
# else:
#     print("X ES MENOR QUE 10")
# print("Fuera del if")

# Ejercicio 2 evaluar más de una condición

x = 10
y = 31

# if x < 10 and y > 30:
#     print("X es menor que 10 y mayor que 30")

# if x < 10 or y > 30:
#     print("X es menor que 10 o y es mayor que 30")

# if not x < 10:
#     print("X no es menor que 10")

# If anidados

is_mayor_edad = True
edad = 17

if is_mayor_edad:
    if edad >= 18:
        print("Tiene la mayoria de edad")
    else:
        print("No tiene la mayoria de edad")
else:
    print("No es mayor de edad")