
numero_a_adivinar = 5
numero_dado_por_usuario = int(input("Tienes 5 oportunidades, adivina el numero: "))
if numero_a_adivinar == numero_dado_por_usuario:
    print("Has ganado")

else:
    print("Has perdido")
    numero_dado_por_usuario = int(input("Te quedan 4 oportunidades, adivina el numero: "))
if numero_a_adivinar == numero_dado_por_usuario:
    print("Has ganado")
else:
    print("Has perdido")
    numero_dado_por_usuario = int(input("Te quedan 3 oportunidades, adivina el numero: "))
if numero_a_adivinar == numero_dado_por_usuario:
    print("Has ganado")
else:
    print("has perdido")
    numero_dado_por_usuario = int(input("Te quedan 2 oportunidades, adivina el numero: "))
if numero_a_adivinar == numero_dado_por_usuario:
    print("Has ganado")
else:
    print("has perdido")
    numero_dado_por_usuario = int(input("Te queda 1 oportunidad, adivina el numero: "))
if numero_a_adivinar == numero_dado_por_usuario:
    print("Has ganado")
else:
    numero_dado_por_usuario = int(input("Te quedaste sin oportunidades."))