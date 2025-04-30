# Agente que analiza el estado emocional del mensaje

from google.adk.agents import Agent

agente_estado_emocional = Agent(
    name="estado_emocional",
    model="gemini-1.5-flash",
    description="Detecta el estado emocional reflejado en el mensaje.",
    instruction="Determina si el mensaje refleja alegría, tristeza, enojo, miedo, etc."
)
