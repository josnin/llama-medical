import uuid, time, glob
import ollama
from langchain_text_splitters import RecursiveCharacterTextSplitter
from chromadb import HttpClient
import settings


chroma = HttpClient(settings.HOST, settings.PORT)
start_time = time.time()

# Handle collection existence efficiently
if not any(collection.name == settings.COLLECTION_NAME for collection in chroma.list_collections()):
    print(f'Creating collection: {settings.COLLECTION_NAME}')
    collection = chroma.get_or_create_collection(
        name=settings.COLLECTION_NAME, metadata={"hnsw:space": "cosine"}
    )
else:
    print(f'Using existing collection: {settings.COLLECTION_NAME}')
    collection = chroma.get_collection(settings.COLLECTION_NAME)

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
    for file in glob.glob(f"{directory}/{settings.MARKDOWN_PATTERN}"):

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
            embed = ollama.embeddings(model=settings.EMBEDDING_MODEL, prompt=chunk.page_content)['embedding']
            collection.add(
                ids=[str(uuid.uuid4())],
                embeddings=[embed],
                documents=[chunk.page_content],
                metadatas={"source": file},
            )
        print(f"{len(chunks)} chunks file {file}")


process_markdown_files(settings.DIRECTORY_PATH)
print(f"total processing time {(time.time() - start_time)} sec")
