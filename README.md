# llama-medical

Local RAG System for Medical Query Exploration (Ollama + LangChain)

This repository explores the potential of a local Retrieval-Augmented Generation (RAG) system for answering medical queries. It uses Ollama for model interaction,  ChromaDB as a local vector store, and LangChain specifically for handling data chunking, focusing on the nomic-embed-text embedding model and the Gemma:2b LLM.



## Getting Started:
[Download & Install Ollama](https://ollama.com/)
```bash
ollama pull nomic-embed-text
ollama pull gemma:2b
ollama serve
```

Install python ollama, langchain, chromadb, etc 
```bash
pip install -r requirements.txt
```

Run chroma db
```bash
chroma run --host localhost --port 8000
```

Run retrieval to import + vectorised medical reference
```python
python retrieval.py
```

Try to ask medical query
```bash
(.venv) josnin@MacBook-Pro llama-medical % python generate.py "what are the causes of kidney stones?"
Sure, here are the causes of kidney stones based on the provided medical text references:

* Diet, excess body weight, some medical conditions, and certain supplements and medications.
* Dehydration.
* Obesity.
* Digestive diseases and surgery.
* Renal tubular acidosis.
* Cystinuria.
* Hyperparathyroidism.
* Repeated urinary tract infections.
```



# Disclaimer
This is an educational project and is not intended for medical diagnosis or treatment. Consult a healthcare professional for any medical concerns.
