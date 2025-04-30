from google.adk.agents import Agent

def dummy_tool(texto: str) -> dict:
    return {"status": "success", "report": f"Echo: {texto}"}

root_agent = Agent(
    name="agente_textos_web",
    model="gemini-1.5-flash",
    description="Agente que responde texto",
    instruction="Responde a los textos que recibe.",
    tools=[dummy_tool]
)
