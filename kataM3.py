# Codigo que imprime una advertencia si un asteroide
# que se aproxime a la tierra
# supera la velocidad de 25 km/h

vel_max = 25 # km/h
ast1 = 49 # el primer asteroide supera vel_max
print("Se aproxima el primer asteroide...")
print("Estar atentos a los mensajes")

if ast1 > vel_max:
    print("PELIGRO. Se aproxima un asteroide a una velocidad muy alta.")
    print("Evacuar el planeta")
elif ast1 == vel_max:
    print("El asteroide se aproxima a la velocidad maxima aceptada")
    print("Tranquilos. Nos salvamos... apenas")
else:
    print("Todos a salvo :)")

print("Se aproxima el segundo asteroide...")
print("Estar atentos a los mensajes")

ast2 = 19 # km/h

if ast2 >= 20:
    print("Atención. Un asteroide se aproxima a una velocidad"+
        +"igual o superior a 20 km/h")
    print("Buscar un rayo de luz en el cielo")
else:
    print("No hay nada que ver aqui")

# Programa con operadores logicos
# Se aproxima un tercer asteroide
print("Se aproxima un tercer asteroide...")
print("Estar atentos a los mensajes")

vel_ast3 = 25
tam_ast3 = 40

if vel_ast3 > 25 and tam_ast3 > 25 and tam_ast3 < 1000:
    print("PELIGRO. Se aproxima un asteroide a una velocidad muy alta.")
    print("Evacuar el planeta")
elif vel_ast3 >= 20:
    print("Buscar un rayo de luz en el cielo")
elif tam_ast3 < 25:
    print("No hay nada que ver")
else:
    print("No hay nada que ver")

print("Fin")
print("Rodrigo Rafael Hurtado Garcia")