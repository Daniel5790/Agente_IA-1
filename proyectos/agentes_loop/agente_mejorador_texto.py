# Agente que mejora un texto basándose en el feedback

from google.adk.agents import Agent

agente_mejorador_texto = Agent(
    name="mejorador_texto",
    model="gemini-1.5-flash",
    description="Mejora un texto basándose en las sugerencias dadas.",
    instruction="Toma el texto y las sugerencias de mejora para reescribirlo mejorándolo."
)
