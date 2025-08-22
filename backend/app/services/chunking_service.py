
from chonkie import RecursiveChunker


def create_document_chunks(text: str, chunk_size: int = 1000):
    chunker = RecursiveChunker(chunk_size=chunk_size)
    chunks = chunker(text)
    return chunks
