# Este agente pule el texto generado aplicando reglas de estilo y claridad.

from google.adk.agents import Agent

agente_pulidor_texto = Agent(
    name="pulidor_texto",
    model="gemini-1.5-flash",
    description="Mejora textos corrigiendo errores y mejorando el estilo.",
    instruction="Corrige errores gramaticales, mejora la fluidez y hace el texto más atractivo."
)
