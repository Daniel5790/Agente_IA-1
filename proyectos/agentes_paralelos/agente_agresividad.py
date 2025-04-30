# Agente que determina si el mensaje es agresivo

from google.adk.agents import Agent

agente_agresividad = Agent(
    name="detector_agresividad",
    model="gemini-1.5-flash",
    description="Detecta si un mensaje contiene un tono agresivo.",
    instruction="Indica si el mensaje es agresivo, pasivo-agresivo o no agresivo."
)
