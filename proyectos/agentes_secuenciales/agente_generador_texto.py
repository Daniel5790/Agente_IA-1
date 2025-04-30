# Este agente genera un texto aleatorio basado en un concepto entregado.

from google.adk.agents import Agent

agente_generador_texto = Agent(
    name="generador_texto",
    model="gemini-1.5-flash",
    description="Genera un texto creativo basado en un concepto dado.",
    instruction="Crea un párrafo corto, imaginativo y bien escrito sobre el concepto entregado."
)
