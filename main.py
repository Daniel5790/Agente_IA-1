from proyectos.agentes_secuenciales.agente_secuencial import ejecutar_agente_secuencial
from proyectos.agentes_paralelos.agente_paralelo import ejecutar_agente_paralelo
from proyectos.agentes_loop.agente_loop import ejecutar_agente_loop

if __name__ == "__main__":
    print("¿Qué tipo de agente deseas ejecutar?")
    print("1. Secuencial")
    print("2. Paralelo")
    print("3. Loop")

    opcion = input("Elige una opción (1/2/3): ")

    if opcion == "1":
        ejecutar_agente_secuencial()
    elif opcion == "2":
        ejecutar_agente_paralelo()
    elif opcion == "3":
        ejecutar_agente_loop()
    else:
        print("Opción no válida.")
