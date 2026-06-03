import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain.agents import create_agent
ruta_env = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=ruta_env)

if os.getenv("GITHUB_TOKEN"):
    print("Archivo .env con GITHUB_TOKEN detectado.")
else:
    print("No se pudo leer el GITHUB_TOKEN.")

def herramienta_consulta(query: str) -> str:
    """Simula una busqueda en una base de datos organizacional"""
    return f"Resultados de la consulta para: '{query}' datos de rendimiento organizacional recuperados de forma exitosa"

def herramienta_escritura(texto: str) -> str:
    """Simula la escritura o guardado de un reporte oficial"""
    return f"El texto '{texto}' ha sido guardado e indexado en el reporte de manera correcta"

tools = [
    Tool(
        name="Consulta_Informacion",
        func=herramienta_consulta,
        description="util para buscar informacion o datos históricos organizacionales"
    ),
    Tool(
        name="Escritura_Reporte",
        func=herramienta_escritura,
        description="Util para redactar, guardar o estructurar informacion en un documento oficial"
    )
]

llm = ChatOpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_TOKEN"),
    model="gpt-4o-mini",
    temperature=0
)

agent_executor = create_agent(llm, tools)

if __name__ == "__main__":
    print("\n=== Iniciando el Agente Organizacional ===")
    
    print("--- Ejecutando Tarea 1 ---")
    respuesta1 = agent_executor.invoke({"messages": [("user", "Busca informacion sobre las metricas de rendimiento del departamento")]})

    datos_metricas = respuesta1["messages"][-1].content
    print("Datos obtenidos de la Tarea 1")

    print("\n--- Ejecutando Tarea 2 ---")
    prompt_reporte = f"""
    Basandote estrictamente en los siguientes datos de rendimiento obtenidos:
    "{datos_metricas}" Redacta el reporte oficial detallado del departamento. 
    REQUISITO OBLIGATORIO: Debe ser un informe técnico, formal, que incluya una estructura con introduccion, desarrollo con viñetas, numeros, 
    porcentajes simulados de cumplimiento de metas y una seccion de conclusiones. No saludes ni des confirmaciones de cortesia, escribe directamente el reporte.
    """

    respuesta2 = agent_executor.invoke({"messages": [("user", prompt_reporte)]})

    reporte_final_texto = respuesta2["messages"][-1].content

    print(f"\nRespuesta Final Agente:\n{reporte_final_texto}\n")

    with open("reporte_final.txt", "w", encoding="utf-8") as archivo:
        archivo.write(reporte_final_texto)

print("El reporte oficial se ha guardado con exito en 'reporte_final.txt'")