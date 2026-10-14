from app.services.ingestion import load_file
from app.services.ingestion import chunk_documents
from pathlib import Path
from app.rag.vectorstore import add_documents
doc=load_file(Path("data/sample_kb/IT-Handbook.md"))
chunks=chunk_documents(doc)
add_documents(chunks)
