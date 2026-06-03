# Evaluación Parcial N°2 - Agente Funcional

Este repositorio contiene la implementación de un agente de IA funcional diseñado para integrar herramientas de consulta, escritura y razonamiento dentro de un flujo organizacional

# Agente Organizacional con Github Models
Este proyecto consiste en el desarrollo de un sistema automatizado diseñado para la recopilación de metricas de rendimiento y la generacion de reportes organizacionales. La solucion se implemento utilizando la infraestructura de Github Models como alternativa tecnica para el procesamiento de las consultas

## Requisitos
Hay que tener python instalado y correr este comando en la terminal para instalar las librerias de langchain que se usan:
pip install langchain langchain-core langgraph langchain-openai python-dotenv

## Configuracion
Para que funcione hay que crear un archivo llamado ".env" en la misma carpeta que el "main.py" y poner el token de github que sacas de configuration -> developer settings

GITHUB_TOKEN=ghp_token_aqui

## Como ejecutar
Una vez instalado todo y con el token puesto solo abrir la terminal y poner:

python main.py

El script va a correr la tarea 1 de buscar las metricas y despues la tarea 2 que genera el reporte oficial usando la memoria del agente.