from google.adk.agents import Agent

root_agent = Agent(
    name="construccion_textos_agente",
    model="gemini-1.5-flash",
    description="Agente para construcción, análisis y mejora de textos.",
    instruction="Actúa como un experto en escritura creativa y revisión de textos.",
    tools=[]
)
