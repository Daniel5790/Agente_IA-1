# Agente que extrae el asunto principal del mensaje

from google.adk.agents import Agent

agente_extractor_asunto = Agent(
    name="extractor_asunto",
    model="gemini-1.5-flash",
    description="Extrae el tema principal de un mensaje.",
    instruction="Identifica y resume el asunto principal del mensaje recibido."
)
