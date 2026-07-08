# Evaluacion Parcial 3 - Agente Organizacional (ISY0101)

Este proyecto es la solucion para la Evaluacion Parcial 3. Es un agente para empresas hecho en Python que usa LangChain y el modelo gpt-4o-mini conectado a la API de GitHub Models.

La idea es que el script haga dos tareas seguidas de forma automatica: primero busca informacion de manera segura y midiendo los tiempos, y despues arma un informe cuidando la privacidad de los datos.

---

## Requisitos Previos

Para que funcione es necesario tener estas dos claves guardadas en la computadora:
1. Un token de acceso de GitHub (GITHUB_TOKEN) para poder usar los modelos de inteligencia artificial.
2. Una clave de API de LangChain (LANGCHAIN_API_KEY) para ver el historial de ejecucion en su plataforma.

---

## Configuracion del Entorno

1. Descargar el repositorio y entrar a la carpeta:
   git clone https://github.com/tu-usuario/nombre-del-repositorio.git
   cd nombre-del-repositorio

2. Crear y activar el entorno virtual en Windows (PowerShell):
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     pip install -r requirements.txt

3. Configurar las claves secretas:
   Crear un archivo llamado .env en la carpeta raiz del proyecto y pegar esto:
   GITHUB_TOKEN=tu_token_de_github
   LANGCHAIN_API_KEY=tu_token_de_langsmith

---

## Que hace el codigo exactamente

### Parte 1: Busqueda Segura y Tiempos de Respuesta
1. Bloqueo de seguridad: El codigo revisa lo que le pides a la base de datos y bloquea palabras prohibidas para evitar que se filtre informacion confidencial.
2. Control de tiempo: Mide y muestra en la pantalla cuantos segundos tarda el sistema en responder para saber si esta lento.

### Parte 2: Creacion del Informe y Cuidado de Datos
1. Filtro de privacidad: El programa revisa el texto que escribe la inteligencia artificial y borra automaticamente datos personales como RUTs o sueldos para cumplir las reglas de privacidad.
2. Estructura ordenada: Escribe un documento formal que se divide en Introduccion, Desarrollo (con metas cumplidas) y Conclusion.
3. Explicacion clara: En la parte final, el mismo agente explica con sus palabras el porqué de los resultados obtenidos para que todo sea transparente.

---

## Como correr el programa

1. Ejecutar el archivo principal:
   Abre la terminal del editor y escribir este comando:
   python main.py

2. Que se va a ver en la pantalla:
   * Apareceran mensajes marcados con un TRACE ID para seguir el orden de lo que pasa.
   * Veras mensajes de conexion exitosa como HTTP 200 OK.
   * El texto del informe final saldra impreso en la terminal y se guardara solo en un archivo nuevo llamado reporte_final.txt.