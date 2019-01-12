
mayoriaedad = 18
print("Bienvenido a la DISCO ")
print("Solo pueden ingresar mayores de edad")
edad_usuario = (int(input("Por favor, ingrese su edad: ")))

if edad_usuario >= 18:
    print("Bienvenido,disfrute su estadia")
else:
    faltante = mayoriaedad - edad_usuario
    if faltante == 1:
        years = " año."
    else:
        years = " años."
    print("Lo sentimos, no puedes ingresar.")
    print("Puede volver dentro de: {}{}".format(faltante, years))

