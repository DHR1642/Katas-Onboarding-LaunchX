print("Ejercicio 1")

def genera_reporte(t1, t2, t3):
    promedio = (t1+t2+t3)/3
    return f"""Reporte de tanques:
    Promedio de los tres tanques:{promedio}
    Tanque principal: {t1}
    Tanque externo: {t2}
    Tanque de hidrógeno: {t3}
    """
print(genera_reporte(10,2,34))

def calc_promedio(valores): # recibe una lista
    total = sum(valores)
    for i in valores:
        total += i
    return total/len(valores)

print("Ahora con la otra función: ")

def genera_reporte2(t1, t2, t3):
    promedio = calc_promedio([t1,t2,t3])
    return f"""Reporte de tanques:
    Promedio de los tres tanques:{promedio}
    Tanque principal: {t1}
    Tanque externo: {t2}
    Tanque de hidrógeno: {t3}
    """
print(genera_reporte(10,34,2))

print("Ejercicio 2")

def informe_cohete(tiempo_previo, tiempo_vuelo, destino, tanque_externo, tanque_principal):
    return f"""
    Misión hacia: {destino}
    Tiempo total de viaje: {tiempo_vuelo+tiempo_previo} min.
    Combustible disponble: {tanque_externo+tanque_principal} galones.
    """

print(informe_cohete(124,54,"Luna", 200000, 300000))

def informe_cohete2(destino, *minutos, **reservas_combustible):
    reporte = f"""
    Misión hacia: {destino}
    Tiempo total de viaje: {sum(minutos)} min.
    Combustible disponble: {sum(reservas_combustible.values())} galones.
    """
    for i,j in reservas_combustible.items():
        reporte += f"tanque {i} tiene: {j} galones restantes.\n"
    return reporte
print(informe_cohete2("Luna",124,54,13, principal=300000, externo =50001))
print("FIN")
# Rodrigo Rafael Hurtado García