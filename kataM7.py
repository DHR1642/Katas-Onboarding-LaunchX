from time import sleep

# Ejercicio 1
planeta_nuevo = ""
planetas = []
while planeta_nuevo.lower() != "listo":
    if planeta_nuevo:
        planetas.append(planeta_nuevo)
    planeta_nuevo = input("Ingresa el nombre de un planeta. Teclea 'listo' al terminar: ")

# Ejercicio 2

for p in planetas:
    print(p)
print("Fin")

# Rodrigo Rafael Hurtado García