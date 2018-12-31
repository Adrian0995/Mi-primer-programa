

pokemon_elegido = input("¿Que pokemon quieres elegir para el combate? (Squirtle / Charmander / Bulbaseur): ")

vida_pikachu = 100
vida_enemigo= 0
ataque_pokemon= 0
if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    nombre_pokemon= "Squirtle"
    ataque_pokemon= 12

elif pokemon_elegido == "Charmander":
    vida_enemigo= 80
    nombre_pokemon= "Charmander"
    ataque_pokemon= "8"

elif pokemon_elegido =="Bulbaseur":
    vida_enemigo=100
    nombre_pokemon="Bulbaseur"
    ataque_pokemon="6"

while vida_pikachu >0 and vida_enemigo >0:
    ataque_elegido = input("¿Que ataque usaras contra el enemigo? (Trueno / Cola de hierro):")
    if ataque_elegido == "Trueno":
        print("Has usado Trueno y le has quitado 10 puntos de vida a tu rival")
        vida_enemigo -= 10
    elif ataque_elegido == "Cola de hierro":
        print("Has usado Cola de hierro y le has quitado 12 puntos de vida a tu rival")
        vida_enemigo -= 12

    print("La vida de {} es de {} ".format(nombre_pokemon, vida_enemigo))

    print("{} te hace un ataque de {}".format(nombre_pokemon , ataque_pokemon))
    vida_pikachu -= ataque_pokemon
    print("La vida restante de Pikachu es: {}".format(vida_pikachu))

if vida_enemigo<=0:
    print("Has ganado")
if vida_pikachu<=0:
    print("Has perdido")

print("El combate ha terminado")