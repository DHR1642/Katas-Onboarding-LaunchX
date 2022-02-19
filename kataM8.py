print("Ejercicio 1")
# Crear diccionario sobre el planeta Marte

planeta = {
    "nombre" : "Marte",
    "lunas" : 2 
}

print(planeta.get("nombre"), "tiene",
    planeta["lunas"], "lunas.")

planeta.update({"circunferencia (km)" :
           {"polar":6752,
            "ecuatorial":6792} })
print(f"{planeta['nombre']} tiene una circunferencia polar de: {planeta['circunferencia (km)']['polar']} km.")

print("Ejercicio 2")

lunas_planetas = {
    'Mercurio': 0,
    'Venus': 0,
    'Tierra': 1,
    'Marte': 2,
    'Júpiter': 79,
    'Saturno': 82,
    'Urano': 27,
    'Neptuno': 14,
    'Plutón': 5,
    'Haumea': 2,
    'Makemake': 1,
    'Eris': 1
}

total_lunas = 0
for value in lunas_planetas.values():
    total_lunas += value
print(f"No. total de lunas = {total_lunas}.")

total_planetas = len(lunas_planetas.keys())
print(f"No. total de planetas = {total_planetas}.")

prom_lunas = total_lunas/total_planetas

print(f"El promedio de lunas por planeta es: {prom_lunas}.")
print("FIN")
# Rodrigo Rafael Hurtado García