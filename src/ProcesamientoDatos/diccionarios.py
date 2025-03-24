# diccionario de números

numeros = {1: "uno",
           2: "dos",
           3: "tres",
           4: "cuatro"}

print(numeros)
# INGRESAR A UNA POSICIÓN DENTRO DE UN DICCIONARIO
print(numeros[4])

# DICCIONARIOS DE INFORMACIÓN PERSONAS

persona = {"nombre": "Alejandro",
           "apellido": "Sastoque",
           "edad": 25,
           "altura": 1.83,}

print(persona)
# del persona["edad"]
print(persona)
print(type(persona))

claves = persona.keys()
print(claves)

values = persona.values()
print(values)

informacion = persona.items()
print(informacion)

contactos_personas = {"Alejandro": {
           "apellido": "Sastoque",
           "edad": 25,
           "altura": 1.83},
           "Juan":{
           "apellido": "Perez",
           "edad": 35,
           "altura": 1.63}}

print(contactos_personas)
print(contactos_personas["Juan"])
print(contactos_personas["Juan"]["apellido"])