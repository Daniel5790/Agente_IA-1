# Agente que genera un primer borrador de texto

from google.adk.agents import Agent

agente_generador_borrador = Agent(
    name="generador_borrador",
    model="gemini-1.5-flash",
    description="Genera un borrador inicial de un texto sobre un tema.",
    instruction="Escribe un texto introductorio o borrador basado en un tema dado."
)
