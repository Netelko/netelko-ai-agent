# NETELKO AI Agent

## Descripción general

NETELKO AI Agent es un asistente de inteligencia artificial basado en la arquitectura **Retrieval-Augmented Generation (RAG)**, desarrollado con **Python**, **LangChain** y **FastAPI**.

El agente responde preguntas utilizando exclusivamente la información contenida en documentos proporcionados por el usuario, como archivos **PDF** y **CSV**. Para ello, convierte el contenido de los documentos en representaciones vectoriales (embeddings), almacena dicha información en una base de datos vectorial y recupera los fragmentos más relevantes para generar respuestas precisas mediante un modelo de lenguaje.

El proyecto fue diseñado para ejecutarse localmente utilizando **Ollama** y está preparado para su despliegue en **Oracle Cloud Infrastructure (OCI)**.

---

# Arquitectura de la solución

```text
                           Usuario
                              │
                              ▼
                     FastAPI REST API
                              │
                              ▼
                        RAG Service
                              │
                              ▼
                        LangChain LCEL
                              │
            ┌─────────────────┴─────────────────┐
            ▼                                   ▼
      Retriever                          Modelo LLM
            │                              (Ollama)
            ▼                                   │
      Chroma Vector DB                          ▼
            │                          Qwen2.5:7B
            ▼
   Embeddings (BAAI/bge-m3)
            │
            ▼
      Documentos PDF / CSV
```

### Flujo de procesamiento

1. El usuario carga documentos PDF o CSV.
2. Los documentos se dividen en fragmentos (chunks).
3. Se generan embeddings utilizando **BAAI/bge-m3**.
4. Los embeddings se almacenan en **ChromaDB**.
5. El usuario realiza una pregunta.
6. El Retriever recupera los fragmentos más relevantes.
7. El modelo **Qwen2.5** genera una respuesta basada únicamente en el contexto recuperado.
8. La API devuelve la respuesta junto con las fuentes utilizadas.

---

# Tecnologías y herramientas utilizadas

* Python 3.13
* FastAPI
* LangChain
* LangChain LCEL
* Ollama
* Qwen2.5:7B
* HuggingFace Embeddings
* BAAI/bge-m3
* ChromaDB
* Pydantic
* Docker
* Git
* GitHub

---

# Estructura del proyecto

```text
netelko-ai-agent/
│
├── app/
│   ├── api/
│   ├── models/
│   ├── services/
│   ├── loaders.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── retriever.py
│   ├── rag_chain.py
│   ├── llm.py
│   └── config.py
│
├── chroma_db/
├── data/
│   └── documents/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Instrucciones para ejecutar el proyecto

## 1. Clonar el repositorio

```bash
git clone https://github.com/Netelko/netelko-ai-agent.git

cd netelko-ai-agent
```

---

## 2. Crear el entorno virtual

```bash
python -m venv .venv
```

Activar el entorno:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Instalar Ollama

Descargar Ollama desde:

https://ollama.com

Descargar el modelo:

```bash
ollama pull qwen2.5:7b
```

---

## 5. Agregar documentos

# Ejecución con Docker

## Requisitos

* Docker Desktop
* Docker Compose

Verificar la instalación:

```bash
docker --version
docker compose version
```

## Construir la imagen

Desde la raíz del proyecto ejecutar:

```bash
docker compose build
```

## Levantar los contenedores

```bash
docker compose up -d
```

## Verificar los contenedores

```bash
docker ps
```

Deberán aparecer al menos los siguientes servicios:

* `netelko-ai-agent`
* `ollama`

## Descargar el modelo en Ollama

La primera vez es necesario descargar el modelo dentro del contenedor:

```bash
docker exec -it ollama ollama pull qwen2.5:7b
```

## Acceder a la API

Swagger:

```text
http://localhost:8000/docs
```

Health Check:

```text
http://localhost:8000/health
```

---

# Ejemplos de preguntas

El agente puede responder preguntas como:

* ¿Qué servicios ofrece NETELKO?
* ¿Dónde se encuentra ubicada la empresa?
* ¿Cuál es la cobertura de los servicios?
* ¿Qué tecnologías utiliza NETELKO?
* ¿Qué ventajas competitivas ofrece la empresa?
* ¿Cómo puedo contactar al área comercial?
* Resume el portafolio de servicios.
* ¿Qué soluciones de telecomunicaciones ofrece la compañía?

---

# Ejemplos de respuestas

### Pregunta

> ¿Qué servicios ofrece NETELKO?

### Respuesta

> NETELKO ofrece soluciones integrales en tecnologías de la información y telecomunicaciones, incluyendo servicios de diseño, implementación, soporte y acompañamiento tecnológico para empresas. Además, cuenta con cobertura regional, alianzas con fabricantes líderes y un enfoque consultivo orientado a las necesidades del cliente.

Fuentes:

* Portafolio de Servicios.pdf (Página 2)
* Portafolio de Servicios.pdf (Página 3)

---

### Pregunta

> ¿Dónde está ubicada NETELKO?

### Respuesta

> NETELKO tiene su sede principal en Bogotá, Colombia, desde donde presta servicios a clientes en toda la región.

Fuente:

* Portafolio de Servicios.pdf (Página 2)

---

# Despliegue en Oracle Cloud Infrastructure (OCI)

> **Estado:** En implementación.

El proyecto está diseñado para ejecutarse en Oracle Cloud Infrastructure (OCI) utilizando servicios administrados.

La arquitectura objetivo es:

```text
Internet
    │
    ▼
Load Balancer
    │
    ▼
Container Instance
    │
    ▼
NETELKO AI Agent
    │
    ├── OCI Generative AI
    └── ChromaDB
```

## Pasos previstos para el despliegue

1. Crear un Compartimento (Compartment).
2. Configurar usuarios y políticas de IAM.
3. Crear un repositorio en Oracle Container Registry (OCIR).
4. Construir la imagen Docker.
5. Etiquetar la imagen para OCIR.
6. Publicar la imagen en OCIR.
7. Crear un Container Instance.
8. Configurar las variables de entorno.
9. Conectar el agente con OCI Generative AI.
10. Validar la API mediante los endpoints `/health` y `/chat`.

---


