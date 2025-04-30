from proyectos.agentes_secuenciales.agente_generador_texto import agente_generador_texto
from proyectos.agentes_secuenciales.agente_pulidor_texto import agente_pulidor_texto
from proyectos.agentes_secuenciales.agente_generador_titulo import agente_generador_titulos

def ejecutar_agente_secuencial():
    """
    Ejecuta el flujo de agentes de forma secuencial.
    """
    concepto = input("Ingrese un concepto para el texto: ")

    # Paso 1: Generar texto
    respuesta_texto = agente_generador_texto.start({"input": concepto})
    texto_generado = respuesta_texto.output
    print(f"\nTexto generado:\n{texto_generado}\n")

    # Paso 2: Pulir texto
    respuesta_pulido = agente_pulidor_texto.start({"input": texto_generado})
    texto_pulido = respuesta_pulido.output
    print(f"\nTexto pulido:\n{texto_pulido}\n")

    # Paso 3: Crear título
    respuesta_titulo = agente_generador_titulos.start({"input": texto_pulido})
    titulo = respuesta_titulo.output
    print(f"\nTítulo sugerido:\n{titulo}\n")
