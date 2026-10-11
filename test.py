from app.rag.embedding import get_embeddings

embeddings = get_embeddings()

voctor = embeddings.embed_query("What is RAG?")

print("vector length:", len(voctor))

print("vector:", voctor[0:10])