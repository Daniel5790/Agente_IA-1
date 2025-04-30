from google.adk.agents import Agent

agente_generador_titulos = Agent(
    name="generador_titulos",
    model="gemini-1.5-flash",
    description="Genera un título creativo basado en un texto.",
    instruction="Crea un título llamativo y breve que resuma el texto entregado."
)
