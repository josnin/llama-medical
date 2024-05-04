# llama-medical

Local RAG System for Medical Query Exploration (Ollama + LangChain)

This repository explores the potential of a local Retrieval-Augmented Generation (RAG) system for answering medical queries. It uses Ollama for model interaction,  ChromaDB as a local vector store, and LangChain specifically for handling data chunking, focusing on the nomic-embed-text embedding model and the Gemma:2b LLM.



# Getting Started:
```bash
download & install ollama, see ref
ollama pull nomic-embed-text
ollama pull gemma:2b

pip install -r requirement

run chroma db
chroma run --host localhost --port 8000
```

# Disclaimer
This is an educational project and is not intended for medical diagnosis or treatment. Consult a healthcare professional for any medical concerns.