# Ejercicio 1
# Programa para calcular la distancia entre dos planetas
# Los planetas se consideran alineados en un mismo eje

dSolTierra = 149597870 # km
dSolJupiter = 778547200 # km

res_km = abs(dSolTierra-dSolJupiter) #km
res_millas = float(res_km)/1.60934 # millas

print(f"La distancia entre la Tierra y Júpiter es: {res_km} km = {res_millas} mi.")
input("Presiona ENTER para continuar al siguiente ejercicio")

# Ejercicio 2
p1 = int(input("Hola usuario. Introduce la distancia entre el Sol y tu planeta en km: "))
p2 = int(input("Ahora introduce la distancia entre el Sol y el otro planeta en km: "))
print("Calculando...")
r_km = abs(p1-p2)
r_mi = float(r_km)/1.60934

print(f"La distancia entre tus dos planetas es: {r_km} km = {r_mi} mi.")