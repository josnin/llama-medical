import sys
import ollama
import chromadb
import settings

def answer_medical_query(query):
    chroma = chromadb.HttpClient(host=settings.HOST, port=settings.PORT)
    collection = chroma.get_or_create_collection(settings.COLLECTION_NAME)
    query_embed = ollama.embeddings(model=settings.EMBEDDING_MODEL, prompt=query)['embedding']
    res = collection.query(query_embeddings=[query_embed], n_results=10)["documents"][0]
    source = "\n\n".join(res)
    prompt_template = f"{query}, only answer the question accurately based on the provided medical text references: '{source}'"
    stream = ollama.generate(model=settings.MODEL, prompt=prompt_template, stream=True)
    return ''.join(chunk["response"] for chunk in stream if chunk["response"])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python generate.py "<query>"')
        sys.exit(1)
    query = " ".join(sys.argv[1:])
    answer = answer_medical_query(query)
    print(answer)
