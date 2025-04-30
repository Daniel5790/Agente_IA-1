from proyectos.agentes_paralelos.agente_extractor_asunto import agente_extractor_asunto
from proyectos.agentes_paralelos.agente_estado_emocional import agente_estado_emocional
from proyectos.agentes_paralelos.agente_agresividad import agente_agresividad

def ejecutar_agente_paralelo():
    mensaje = input("Ingrese un mensaje para analizar: ")
    flujo_paralelo(mensaje)

def flujo_paralelo(mensaje):
    # Analizamos el mensaje en paralelo
    respuesta_asunto = agente_extractor_asunto.start({"input": mensaje})
    asunto = respuesta_asunto.output

    respuesta_estado = agente_estado_emocional.start({"input": mensaje})
    estado = respuesta_estado.output

    respuesta_agresividad = agente_agresividad.start({"input": mensaje})
    agresividad = respuesta_agresividad.output

    print(f"\nAsunto detectado: {asunto}")
    print(f"Estado emocional: {estado}")
    print(f"Agresividad detectada: {agresividad}")

if __name__ == "__main__":
    ejecutar_agente_paralelo()
