PROYECTO: AGENTES IA CON GOOGLE ADK (INTERFAZ DE CONSOLA)

Este proyecto contiene tres tipos de agentes IA que funcionan en español usando Google ADK. Cada uno representa un flujo distinto de trabajo con agentes:

1. Agente Secuencial: genera un texto, luego lo pule, y finalmente le da un título.
2. Agente Paralelo: analiza un mensaje desde múltiples ángulos al mismo tiempo.
3. Agente Loop: revisa y mejora un texto hasta que sea aprobado.

---------------------------------------------------------------------
ESTRUCTURA DEL PROYECTO
---------------------------------------------------------------------

AGENTESIA/
│
├── agenteIA/                       -> Entorno virtual (NO subir al repositorio)
│
├── proyectos/
│   ├── agente_web/                -> Agente base para consola bonita (adk run .)
│   │   ├── agent.py               -> Código del agente raíz
│   │   ├── agent.yaml             -> Configuración ADK
│   │   └── .env                   -> Clave API de Google AI
│   │
│   ├── agentes_loop/             -> Agente tipo loop
│   │   ├── __init__.py
│   │   ├── agente_loop.py
│   │   ├── agente_generador_borrador.py
│   │   ├── agente_revisor_texto.py
│   │   └── agente_mejorador_texto.py
│   │
│   ├── agentes_paralelos/        -> Agente tipo paralelo
│   │   ├── __init__.py
│   │   ├── agente_paralelo.py
│   │   ├── agente_agresividad.py
│   │   ├── agente_estado_emocional.py
│   │   └── agente_extractor_asunto.py
│   │
│   └── agentes_secuenciales/     -> Agente tipo secuencial
│       ├── __init__.py
│       ├── agente_secuencial.py
│       ├── agente_generador_texto.py
│       ├── agente_pulidor_texto.py
│       └── agente_generador_titulo.py
│
├── root_agent.py                 -> (opcional para flujos combinados)
├── main.py                       -> Script de menú para ejecutar agentes desde código
├── requirements.txt              -> Dependencias del proyecto
└── README.txt                    -> Este archivo

---------------------------------------------------------------------
PASOS PARA DEJAR TODO FUNCIONANDO DESDE CERO (EN WINDOWS)
---------------------------------------------------------------------
⚠️ Importante para usuarios de Windows
Google ADK necesita crear enlaces simbólicos para los logs. En Windows, eso puede fallar si no ejecutas tu terminal con permisos elevados.

Para evitar errores como [WinError 1314]:

- Cierra VS Code o PowerShell si está abierto.

- Haz clic derecho en el ícono de Visual Studio Code (o tu terminal).

- Selecciona "Ejecutar como administrador".

- Luego activa el entorno y ejecuta normalmente

1. Abrir una terminal en la carpeta raíz del proyecto AGENTESIA.

2. Crear un entorno virtual:
   python -m venv agenteIA

3. Activar el entorno virtual:
   .\agenteIA\Scripts\activate

4. Instalar las dependencias necesarias:
   pip install -r requirements.txt

5. Crear archivo .env dentro de la carpeta:
   proyectos/agente_web/.env

6. Dentro de ese .env, copiar lo siguiente:
   GOOGLE_API_KEY= AQUI SE PONE LA API-KEY
   GOOGLE_GENAI_USE_VERTEXAI=FALSE

7. Para ejecutar el agente desde consola:
   cd proyectos/agente_web
   adk run .

   Esto abrirá un agente interactivo en la consola, con formato tipo:
   user: [tú escribes acá]
   [respuesta del agente]

---------------------------------------------------------------------
REQUISITOS (requirements.txt)

Contenido del archivo requirements.txt:

google-adk==0.3.0
google-generativeai==0.8.5
python-dotenv

---------------------------------------------------------------------
FIN DEL ARCHIVO
---------------------------------------------------------------------