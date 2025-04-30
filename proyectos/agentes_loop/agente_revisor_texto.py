# Agente que revisa y da feedback al texto

from google.adk.agents import Agent

agente_revisor_texto = Agent(
    name="revisor_texto",
    model="gemini-1.5-flash",
    description="Revisa el texto y decide si cumple los criterios de calidad.",
    instruction=(
        "Evalúa si el texto es claro, bien escrito y completo. "
        "Indica si 'APRUEBA' o 'RECHAZA' con sugerencias de mejora si rechaza."
    )
)
