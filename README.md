# llama-medical

Local RAG System for Medical Query Exploration (Ollama + LangChain)

This repository explores the potential of a local Retrieval-Augmented Generation (RAG) system for answering medical queries. It uses Ollama for model interaction,  ChromaDB as a local vector store, and LangChain specifically for handling data chunking, focusing on the nomic-embed-text embedding model and the Gemma:2b LLM.



## Getting Started:
[download & install ollama](https://ollama.com/)
```bash
download & install ollama, see ref
ollama pull nomic-embed-text
ollama pull gemma:2b
ollama serve
```

install python ollama, langchain, chromadb, etc 
```bash
pip install -r requirements.txt
```

run chroma db
```bash
chroma run --host localhost --port 8000
```

run retrieval to import + vectorised medical reference
```python
python retrieval.py
```

try medical query
```bash
(.venv) josnin@MacBook-Pro llama-medical % python generate.py "how our liver function?" 
Sure, here's an accurate answer based on the provided medical text references:

Liver function tests are blood tests used to help find the cause of your symptoms and monitor liver disease or damage. These tests measure the levels of certain enzymes and proteins in your blood. Higher levels of certain enzymes or proteins may indicate liver damage or disease.
```



# Disclaimer
This is an educational project and is not intended for medical diagnosis or treatment. Consult a healthcare professional for any medical concerns.
