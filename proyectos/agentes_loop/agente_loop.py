from proyectos.agentes_loop.agente_generador_borrador import agente_generador_borrador
from proyectos.agentes_loop.agente_revisor_texto import agente_revisor_texto
from proyectos.agentes_loop.agente_mejorador_texto import agente_mejorador_texto

def flujo_loop(tema):
    respuesta_borrador = agente_generador_borrador.start({"input": tema})
    texto_actual = respuesta_borrador.output

    while True:
        print(f"\nTexto actual:\n{texto_actual}\n")

        respuesta_revision = agente_revisor_texto.start({"input": texto_actual})
        resultado_revision = respuesta_revision.output
        print(f"\nResultado de la revisión:\n{resultado_revision}\n")

        if "APRUEBA" in resultado_revision.upper():
            print("\n✅ El texto ha sido aprobado.\n")
            break
        else:
            respuesta_mejora = agente_mejorador_texto.start({"input": f"{texto_actual}\nFeedback: {resultado_revision}"})
            texto_actual = respuesta_mejora.output

def ejecutar_agente_loop():
    tema = input("Ingrese un tema para desarrollar: ")
    flujo_loop(tema)

if __name__ == "__main__":
    ejecutar_agente_loop()
