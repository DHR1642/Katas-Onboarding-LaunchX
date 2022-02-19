# Ejercicio 1

planetas = ["Mercurio", "Venus", "Tierra",
    "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]
print(planetas)

planetas.append("Plutón")
print(len(planetas))
print(planetas[-1])

# Ejercicio 2
planetas.pop()
print(planetas)

p1 = input("Comenzando con mayúscula, introduzca el nombre de un planeta: ")
print(planetas.index(p1))

print("Los planetas que están más cerca del Sol", 
    "que tu planeta son:")
print(planetas[0:planetas.index(p1)])

print("Los planetas que están más lejos del Sol", 
    "que tu planeta son:")
print(planetas[planetas.index(p1)+1:])

# Fin
# Rodrigo Rafael Hurtado García