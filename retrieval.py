import os, uuid, time, glob
import ollama
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from chromadb import HttpClient

load_dotenv()

collection_name = "all_topics"
host = "localhost"
port = 8000
embedding_model = os.getenv("embedding")
chroma = HttpClient(host, port)
directory_path = "markdowns"
markdown_pattern = "*.md"
start_time = time.time()

# Handle collection existence efficiently
if not any(collection.name == collection_name for collection in chroma.list_collections()):
    print(f'Creating collection: {collection_name}')
    collection = chroma.get_or_create_collection(
        name=collection_name, metadata={"hnsw:space": "cosine"}
    )
else:
    print(f'Using existing collection: {collection_name}')
    collection = chroma.get_collection(collection_name)

# Set a reasonable chunk size, just to show.
def process_markdown_files(directory, chunk_size=500, chunk_overlap=50):
    """
    Processes markdown files, creates chunks, generates embeddings,
    and adds them to ChromaDB.

    Args:
        directory (str): Path to directory containing markdown files.
        chunk_size (int, optional): Size of text chunks. Defaults to 500.
        chunk_overlap (int, optional): Overlap between chunks. Defaults to 50.
    """
    for file in glob.glob(f"{directory}/{markdown_pattern}"):

        with open(file, "r") as f:
            text = f.read()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            is_separator_regex=False,
        )
        chunks = text_splitter.create_documents([text])

        for _, chunk in enumerate(chunks):
            embed = ollama.embeddings(model=embedding_model, prompt=chunk.page_content)['embedding']
            collection.add(
                ids=[str(uuid.uuid4())],
                embeddings=[embed],
                documents=[chunk.page_content],
                metadatas={"source": file},
            )
        print(f"{len(chunks)} chunks file {file}")


process_markdown_files(directory_path)
print(f"total processing time {(time.time() - start_time)} sec")
