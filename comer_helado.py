
apetece_helado_input = input("¿Te apetece un helado? (Si/No): ").upper()
if apetece_helado_input=="SI":
    apetece_helado=True
elif apetece_helado_input=="NO":
    apetece_helado= False
else:
    print("Si o no, nada mas")
    apetece_helado=False

tiene_dinero_input = input("¿Tienes dinero para un helado? (Si/No): ").upper()
esta_el_heladero_input = input("¿Está el heladero?) (Si/No): ").upper()
esta_tu_tia_input = input("¿Está tu tía?) (Si/No): ").upper()


tiene_dinero=tiene_dinero_input == "SI"
esta_tu_tia=esta_tu_tia_input == "SI"
puedes_permitirtelo = tiene_dinero or esta_tu_tia
esta_el_heladero= esta_el_heladero_input == "SI"



if apetece_helado and puedes_permitirtelo and esta_el_heladero:
    print("Pues come uno")
else:
    print("Pues nada")

