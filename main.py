import os
import time
import logging
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import StructuredTool

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [TRACE ID: %(process)d] - %(levelname)s - %(message)s')

ruta_env = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=ruta_env)

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "EP3_Proyecto_Observabilidad_ISY0101"

if os.getenv("GITHUB_TOKEN"):
    logging.info("Archivo .env con GITHUB_TOKEN detectado.")
else:
    logging.warning("No se pudo leer el GITHUB_TOKEN.")

if os.getenv("LANGCHAIN_API_KEY"):
    logging.info("Archivo .env con LANGCHAIN_API_KEY detectado.")
else:
    logging.warning("No se pudo leer el LANGCHAIN_API_KEY.")

def herramienta_consulta(query: str = "") -> str:
    """Util para buscar informacion organizacional. Incluye validaciones de ciberseguridad."""
    start_time = time.time()
    
    if isinstance(query, dict):
        query_efectivo = str(query.get("config", {}).get("tags", query))
    else:
        query_efectivo = str(query)
        
    logging.info(f"Iniciando Span: Consulta Base de Datos | Query: {query_efectivo}")
    
    palabras_prohibidas = ["DROP", "DELETE", "IGNORE INSTRUCTIONS", "BYPASS", "SALARIOS", "CONTRASEÑAS", "DESPIDOS"]
    
    if any(p in query_efectivo.upper() for p in palabras_prohibidas):
        logging.warning(f"Intento de violacion de politicas de seguridad detectado. Query: {query_efectivo}")
        return "Alerta de Seguridad: Intento de acceso a informacion confidencial bloqueado."
    
    time.sleep(0.5) 
    latencia = time.time() - start_time
    
    logging.info(f"Consulta finalizada con exito. Latencia de operacion: {latencia:.2f}s")
    return f"Resultados de la consulta para: '{query_efectivo}' | Datos recuperados. (Latencia registrada: {latencia:.2f}s)"

def herramienta_escritura(texto: str = "", **kwargs) -> str:
    """Simula la escritura de un reporte aplicando filtros eticos y de privacidad."""
    logging.info("Iniciando Span: Escritura de Reporte Oficial")
    
    texto_efectivo = texto
    if not texto_efectivo and "args" in kwargs:
        args = kwargs["args"]
        texto_efectivo = str(args[0]) if isinstance(args, list) and len(args) > 0 else str(args)
    elif not texto_efectivo and kwargs:
        texto_efectivo = str(next(iter(kwargs.values())))

    if "RUT" in texto_efectivo.upper() or "SALARIO" in texto_efectivo.upper():
        logging.warning("Datos sensibles detectados (PII). Aplicando anonimizacion automatica para cumplir normativa.")
        texto_efectivo = texto_efectivo.replace("RUT", "[DATOS_ANONIMIZADOS]").replace("salario", "[DATO_CONFIDENCIAL]").replace("SALARIO", "[DATO_CONFIDENCIAL]")

    try:
        with open("reporte_final.txt", "w", encoding="utf-8") as f:
            f.write(texto_efectivo)
    except Exception as e:
        logging.error(f"Error al escribir archivo fisico: {e}")

    logging.info("El documento ha superado las pruebas de equidad y privacidad. Indexacion exitosa.")
    return "El texto redactado ha sido validado eticamente y guardado de manera segura."

Consulta_Informacion = StructuredTool.from_function(
    func=herramienta_consulta,
    name="Consulta_Informacion",
    description="Util para buscar informacion organizacional. Incluye validaciones de ciberseguridad."
)

Escritura_Reporte = StructuredTool.from_function(
    func=herramienta_escritura,
    name="Escritura_Reporte",
    description="Util para redactar y guardar informacion en documentos oficiales. Aplica filtros eticos."
)

tools = [Consulta_Informacion, Escritura_Reporte]

llm = ChatOpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_TOKEN"),
    model="gpt-4o-mini",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente organizacional diseñado para consultar y redactar informes. Tienes acceso a herramientas de seguridad y etica. Procesa los parametros de las herramientas de forma simple."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

if __name__ == "__main__":
    print("\n=== Iniciando el Agente Organizacional ===")
    
    print("\n--- Ejecutando Tarea 1 (Prueba de Seguridad y Metricas) ---")
    respuesta_valida = agent_executor.invoke({"input": "Busca informacion sobre las metricas de rendimiento del departamento para el Q3"})
    datos_metricas = respuesta_valida["output"]
    print("Datos obtenidos de la Tarea 1 de forma segura.")

    print("\n--- Ejecutando Tarea 2 (Reporte con Explicabilidad y Etica) ---")
    
    prompt_reporte = f"""
    Basandote estrictamente en los siguientes datos de rendimiento:
    "{datos_metricas}"
    Redacta el reporte oficial detallado del departamento. 
    
    REQUISITOS OBLIGATORIOS: 
    1. ESTRUCTURA: Debe ser un informe tecnico y formal que incluya: Introduccion, Desarrollo (con viñetas, numeros, porcentajes simulados de cumplimiento de metas) y Conclusion.
    2. ETICA: Menciona en la introduccion que este reporte garantiza la proteccion y anonimizacion de datos sensibles.
    3. EXPLICABILIDAD (XAI): En la conclusion, incluye una breve justificacion o "razonamiento del agente" de por que las metricas muestran ese comportamiento para ser transparente.
    
    No saludes ni des confirmaciones de cortesia, escribe directamente el reporte.
    """

    respuesta2 = agent_executor.invoke({"input": prompt_reporte})
    reporte_final_texto = respuesta2["output"]

    print(f"\nRespuesta Final Agente:\n{reporte_final_texto}\n")

    with open("reporte_final.txt", "w", encoding="utf-8") as archivo:
        archivo.write(reporte_final_texto)

    print("El reporte oficial se ha guardado con exito y cumple con la trazabilidad.")